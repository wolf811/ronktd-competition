from django.urls import include, path

import publications.views as publications

app_name = "publications"

urlpatterns = [
    path("details/<slug:post_pk>/", publications.details, name="details"),
    # path("details", publications.details, name="details"),
]
