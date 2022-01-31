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

main_urls_module = settings.MAIN_URLS_MODULE

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("seminar.urls", namespace="seminar")),
    # path("", include("main.urls", namespace="main")),
    path("seminar/register/", seminar.register_participant, name="seminar_register"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("captcha/", include("captcha.urls")),
    # path("users/", include("users.urls", namespace="users")),
    path("publications/", include("publications.urls", namespace="publications")),
    path("rsps-conf/", include("rsps_conf.urls", namespace="rsps_conf")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""don't forget about settings_deploy_variables.py"""
if main_urls_module:
    urlpatterns += [
        path(
            "",
            include(
                main_urls_module["urls"], namespace=(main_urls_module["namespace"])
            ),
        )
    ]
