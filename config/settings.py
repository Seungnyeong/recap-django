import os
import environ

env = environ.Env()
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

THRID_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "strawberry.django",
    "corsheaders",
]

CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
    "common.apps.CommonConfig",
    "experiences.apps.ExperiencesConfig",
    "categories.apps.CategoriesConfig",
    "reviews.apps.ReviewsConfig",
    "wishlists.apps.WishlistsConfig",
    "bookings.apps.BookingsConfig",
    "medias.apps.MediasConfig",
    "direct_messages.apps.DirectMessagesConfig",
]

SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = SYSTEM_APPS + THRID_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:3000"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

MEDIA_ROOT = "uploads"
MEDIA_URL = "user-uploads/"
PAGE_SIZE = 3

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "config.authentication.JWTAuthentication",
    ],
}

GH_SECRET = env("GH_SECRET")
