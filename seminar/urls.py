from django.urls import include, path

import seminar.views as seminar

app_name = "seminar"

urlpatterns = [
    path("", seminar.index, name="index"),
    path("register/", seminar.index, name="index"),
    path("subscribe/", seminar.index, name="index"),
]
