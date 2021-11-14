from django.urls import include, path

import publications.views as publications

app_name = "main"

urlpatterns = [
    path("details/<slug:post_pk>/", publications.details, name="details"),
    # path("details", publications.details, name="details"),
]
