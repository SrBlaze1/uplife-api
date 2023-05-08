from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class SignUpSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "password2", "date_joined")
        extra_kwargs = {
            "date_joined": {"read_only": True, "format": "%d/%m/%Y %H:%M:%S"},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data["name"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "first_name",
            "email",
            "date_joined",
            "last_login",
        )
        extra_kwargs = {
            "date_joined": {"read_only": True, "format": "%d/%m/%Y %H:%M:%S"},
            "last_login": {"read_only": True, "format": "%d/%m/%Y %H:%M:%S"},
        }

class KnoxSerializer(serializers.Serializer):
   
    token = serializers.CharField()
    expiry = serializers.DateTimeField()
    user = UserSerializer(many=False, read_only=True)