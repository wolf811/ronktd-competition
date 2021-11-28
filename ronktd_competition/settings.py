"""
Django settings for ronktd_competition project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import json
import os
from datetime import timedelta
from pathlib import Path

from .settings_deploy_variables import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "04l2*1__lt%2^lotj)i6#gdki=uv)%i1b57l5*q7818t1^85%-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sass_processor",
    "widget_tweaks",
    "captcha",
    "users",
    "main",
    "publications",
    "gallery",
    "accounts",
    "competitors",
    "crm",
    "operators",
    "partners",
    "cases",
    "contacts",
    "common",
    "seminar",
    "mailings",
    "ckeditor",
    "ckeditor_uploader",
]

# WKHTMLTOPDF_CMD_OPTIONS = {
#     'quiet': False,
# }
# WKHTMLTOPDF_CMD = "xvfb-run -a wkhtmltopdf"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]


CORS_ALLOWED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        # 'rest_framework.permissions.IsAuthenticated',
        "rest_framework.permissions.AllowAny",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework_filters.backends.RestFrameworkFilterBackend",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    # "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}


JWT_AUTH = {
    "JWT_ALLOW_REFRESH": True,
    "JWT_EXPIRATION_DELTA": timedelta(hours=1),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
}

ROOT_URLCONF = "ronktd_competition.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "main.context_processors.profile",
                "main.context_processors.csrf",
                "seminar.context_processors.active_seminar",
            ],
        },
    },
]

WSGI_APPLICATION = "ronktd_competition.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    # TODO: https://www.pgbouncer.org/usage.html
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ronktd_competition_db",
        "USER": "ronktd_competition_db_user",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

###AUTH DEFAULT PAGE###
LOGIN_URL = "/edo/"
#######################


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "email/messages"

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 6,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.CustomUser"


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static_root/"
SASS_PROCESSOR_ENABLED = True
SASS_PROCESSOR_AUTO_INCLUDE = False
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r"^.+\.scss$"
# SASS_OUTPUT_STYLE = 'compact'

SASS_PRECISION = 10
SASS_ROOT = os.path.join(BASE_DIR, "assets")
SASS_PROCESSOR_ROOT = SASS_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "assets"),
)

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, "assets", "scss"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# import pdb; pdb.set_trace()

# QR_CODE_CHECK_URL = "http://acnk.naks.ru/qr-code-check/"

# WEBPACK_URL='/webpackbundles/'
# WEBPACK_ROOT=os.path.join(BASE_DIR, 'webpackbundles')

####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "examen_db": {
        "skin": "minimalist",
        "width": "100%",
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
    },
    "default": {
        "toolbar": [
            [
                "Undo",
                "Redo",
                "-",
                "Bold",
                "Italic",
                "Underline",
                "-",
                "Link",
                "Unlink",
                "Anchor",
                "-",
                "Format",
                "-",
                "Maximize",
                "-",
                "Table",
                "-",
                "Image",
                "-",
                "Source",
                "-",
                "NumberedList",
                "BulletedList",
            ],
            [
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
                "-",
                "Font",
                "FontSize",
                "TextColor",
                "-",
                "Outdent",
                "Indent",
                "-",
                "HorizontalRule",
                "-",
                "Blockquote",
            ],
        ],
        "skin": "moono",
        "forcePasteAsPlainText": True,
        "format_tags": "p;h1;h2;h3;pre",
        "contentsCss": [
            "/static/css/ckeditor_init.css",
        ],
        "stylesSet": [
            {"name": "Строчный код", "element": "code"},
            {
                "name": "Скрыть для мобильных",
                "element": "span",
                "attributes": {"class": "hide_for_mobile"},
            },
            {
                "name": "Монолитный элемент",
                "element": "span",
                "attributes": {"style": "white-space: nowrap;"},
            },
            {
                "name": "Адаптивная таблица",
                "element": "div",
                "attributes": {"class": "table-responsive"},
            },
        ],
        "fontSize_sizes": "8/8px;9/9px;10/10px;11/11px;12/12px;13/13px;14/14px;15/15px;16/16px;17/17px;18/18px;19/19px;20/20px;"
        "21/21px;22/22px;23/23px;24/24px;25/25px;26/26px;27/27px;28/28px;36/36px;48/48px;72/72px;1/1px;",
    },
}


####################################
###  DJANGO-RESIZED CONFIGURATION ##
####################################
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = "JPEG"
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {"JPEG": ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True


home = str(Path.home())
# import pdb; pdb.set_trace()
# with open(os.path.join('/', 'home', 'popov', 'send_mail_secret.json'), 'r') as f:
with open(os.path.join(home, "send_mail_secret.json"), "r") as f:
    json_email_settings = f.read()
    email_settings = json.loads(json_email_settings)
    EMAIL_HOST = email_settings["EMAIL_HOST"]
    EMAIL_PORT = email_settings["EMAIL_PORT"]
    EMAIL_HOST_USER = email_settings["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = email_settings["EMAIL_HOST_PASSWORD"]


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_SSL = True


if "installed_server_apps" in locals():
    INSTALLED_APPS += installed_server_apps
