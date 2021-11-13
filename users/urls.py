from django.urls import path

import users.views as users

# from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("login/", users.login_classic, name="login"),
    # path("logged-in/", users.logged_in, name="logged-in"),
    # path("logout/", users.logout_user, name="logout"),
    # path("register/", users.register, name="register"),
]
