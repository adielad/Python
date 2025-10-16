from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(BASE_DIR / ".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "dev-secret-key-change-me",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "1") not in {"0", "false", "False"}

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
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
        "DIRS": [BASE_DIR / "web" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# Databases: SQLite for Django by default; optional separate 'mssql' for querying
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if os.environ.get("MSSQL_SERVER"):
    DATABASES["mssql"] = {
        "ENGINE": "mssql",
        "NAME": os.environ.get("MSSQL_DATABASE", "master"),
        "USER": os.environ.get("MSSQL_USER", "sa"),
        "PASSWORD": os.environ.get("MSSQL_PASSWORD", ""),
        "HOST": os.environ.get("MSSQL_SERVER", "localhost"),
        "PORT": os.environ.get("MSSQL_PORT", "1433"),
        "OPTIONS": {
            "driver": os.environ.get("MSSQL_ODBC_DRIVER", "ODBC Driver 18 for SQL Server"),
            "trustServerCertificate": os.environ.get("MSSQL_TRUST_CERT", "yes"),
            # allows arbitrary extra connection string parameters
            # e.g. in .env: MSSQL_EXTRA_PARAMS=Encrypt=no;TrustServerCertificate=yes
            "extra_params": os.environ.get("MSSQL_EXTRA_PARAMS", ""),
        },
    }

# Use cookie-based sessions to avoid DB migrations for sessions in dev
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = os.environ.get("TZ", "UTC")
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
