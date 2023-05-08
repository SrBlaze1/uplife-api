from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
)
from rest_framework.exceptions import AuthenticationFailed

from users.models import User
from users.serializers import SignUpSerializer, UserSerializer

from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from knox.views import LogoutAllView as KnoxLogoutAllView
from knox.models import AuthToken
from knox.auth import TokenAuthentication

from django.contrib.auth.signals import user_logged_in
from django.utils import timezone

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Authentication"])
class SignUpView(CreateAPIView):  # Register a user
    """
    Signup a user.
    Credentials must be posted via post request (json)
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer
    authentication_classes = ()


@extend_schema(tags=["Authentication"])
class LoginView(KnoxLoginView):  # Login a user
    """
    Logs in a user.
    Credentials must be provided via *Basic HTTP authentication*.
    """

    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication,)

    def post(self, request, format=None):  # Modification of knox.views.LoginView
        token_limit_per_user = self.get_token_limit_per_user()

        if token_limit_per_user is not None:
            now = timezone.now()
            try:
                token = request.user.auth_token_set.filter(expiry__gt=now)
            except:
                raise AuthenticationFailed("Invalid or non existing credentials.")
            if token.count() >= token_limit_per_user:
                return Response(
                    {"error": "Maximum amount of tokens allowed per user exceeded."},
                    status=HTTP_403_FORBIDDEN,
                )

        token_ttl = self.get_token_ttl()
        instance, token = AuthToken.objects.create(request.user, token_ttl)
        user_logged_in.send(
            sender=request.user.__class__, request=request, user=request.user
        )

        data = self.get_post_response_data(request, token, instance)

        response = Response(data)
        response.set_cookie(
            "auth_token", token, httponly=True, samesite="strict"
        )  # Only change made on the default method

        return response


@extend_schema(tags=["Authentication"])
class UserView(APIView):  # Get user info
    """
    Get details of logged user
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)


@extend_schema(tags=["Authentication"])
class LogoutView(KnoxLogoutView):
    """
    Logout currently logged user (Revokes provided Token)
    """

    pass


@extend_schema(tags=["Authentication"])
class LogoutAllView(KnoxLogoutAllView):
    """
    Logout currently logged user from all instances (Revokes all user's Tokens)
    """

    pass
