from django.urls import path, include
import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    # path("agreement/", main.agreement, name="agreement"),
    # path("profile/", main.profile, name="profile"),
    # path("examples/", main.examples, name="examples"),
    # path("authorization/", main.authorization, name="authorization"),
    # path("register/", main.register, name="register"),
]
