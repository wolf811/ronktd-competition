"""oip_naks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import seminar.views as seminar
from django.conf import settings
# from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("main.urls", namespace="main")),
    path("", include("seminar.urls", namespace="seminar")),
    path("seminar/register/", seminar.register_participant, name="seminar_register"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("captcha/", include("captcha.urls")),
    # path("users/", include("users.urls", namespace="users")),
    path("publications/", include("publications.urls", namespace="publications")),
    # path("seminar/", include("seminar.urls", namespace="seminar")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
