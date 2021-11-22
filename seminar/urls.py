from django.urls import include, path

import seminar.views as seminar

app_name = "seminar"

urlpatterns = [
    path("", seminar.index, name="index"),
]
