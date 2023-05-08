import users.views as views
from django.urls import path


urlpatterns = [
    path("user", views.UserView.as_view(), name="user"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("logoutall", views.LogoutAllView.as_view(), name="logoutall"),
]
