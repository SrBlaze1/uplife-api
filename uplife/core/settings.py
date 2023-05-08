# Importing necessary packages
from pathlib import Path
import os
import environ
import dj_database_url
from datetime import timedelta
from rest_framework.settings import api_settings

# Setting up django-environ to read environment variables
env = environ.Env()
environ.Env.read_env()

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Setting the static file URL and root directories
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Setting the media file URL and root directories
MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
MEDIA_URL = "/media/"

# Retrieving the SECRET_KEY from environment variables
# Avoid explicitly storing sensitive information like secret keys
SECRET_KEY = env("SECRET_KEY")

# Debug mode settings
DEBUG = env("DEBUG") or False

# Specifying the allowed hosts
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Specifying trusted origins for CSRF
CSRF_TRUSTED_ORIGINS = [env("CSRF_TRUSTED_ORIGINS")]
# Setting CSRF_COOKIE_SECURE to True for enhanced security
CSRF_COOKIE_SECURE = True

# List of installed apps
INSTALLED_APPS = [
    "authtools",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "knox",
    "drf_spectacular",
    "corsheaders",
    "users",
    "recipients",
    "donations",
]

# Setting the SITE_ID
SITE_ID=1

# List of middleware used
MIDDLEWARE = [
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# Configuring Whitenoise for serving static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Setting the root URL configuration
ROOT_URLCONF = "core.urls"

# Setting up the Django templates engine
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# List of authentication backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Setting up the WSGI application
WSGI_APPLICATION = "core.wsgi.application"

# Setting up the database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Loading database configuration from environment variables
db_from_env = dj_database_url.config(conn_max_age=500, conn_health_checks=True)
DATABASES["default"].update(db_from_env)

# List of authentication password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"


# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = "pt-BR"
TIME_ZONE = "America/Sao_Paulo"

DATE_INPUT_FORMATS = ["%d/%m/%Y"]
TIME_INPUT_FORMATS = ["%H:%M:%S"]
USE_I18N = True
USE_TZ = True
USE_L10N = False

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
X_FRAME_OPTIONS = "SAMEORIGIN"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Default authentication scheme
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DATETIME_FORMAT": f"{DATE_INPUT_FORMATS[0]} {TIME_INPUT_FORMATS[0]}",
}


# Token Auth
REST_KNOX = {
    "SECURE_HASH_ALGORITHM": "cryptography.hazmat.primitives.hashes.SHA512",
    "AUTH_TOKEN_CHARACTER_LENGTH": 64,
    "TOKEN_TTL": timedelta(days=1),
    "USER_SERIALIZER": "knox.serializers.UserSerializer",
    "TOKEN_LIMIT_PER_USER": 5,
    "AUTO_REFRESH": False,
    "EXPIRY_DATETIME_FORMAT": api_settings.DATETIME_FORMAT,
}


# Docs
SPECTACULAR_SETTINGS = {
    # Schema Info
    "TITLE": "UpLife",
    "DESCRIPTION": "UpLife API",
    "VERSION": "0.0.1",
    "TAGS": [
        {"name": "Recipient Management | Institution", "description": "Manage Recipient Institutions"},
        {"name": "Recipient Management | Bag", "description": "Manage Recipient Bag Types"},
        {"name": "Recipient Management | Medicine", "description": "Manage Recipient Accepted Medicines"},
        
        {"name": "Donation Management | Blood", "description": "Manage Blood Donations"},
        {"name": "Donation Management | Medicine", "description": "Manage Medicine Donations"},
        {"name": "Donation Management | Appointment", "description": "Manage Donation Appointments"},
        {"name": "Authentication", "description": "User Access/Creation"},
    ],
    "SERVERS": [
        {"url": env("CSRF_TRUSTED_ORIGINS"), "description": "Localhost/Dev server"}
    ],
    "CONTACT": {"name": "API Support"},
    # Schema Settings
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
    "COMPONENT_SPLIT_PATCH": True,
    "SERVE_PUBLIC": True,
    "DISABLE_ERRORS_AND_WARNINGS": True,
}