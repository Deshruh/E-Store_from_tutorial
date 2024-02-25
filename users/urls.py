from django.urls import path

from users import views


app_name = "urls"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]
