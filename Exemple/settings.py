from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Clé secrète (ne pas exposer en prod)
SECRET_KEY = "django-insecure-3)&8!#m)@r#k8gup3(d8h@f@%5z2^k^i6#p52^oa4fthfsi$zj"

DEBUG = True

ALLOWED_HOSTS = [
    'studiovisiocom-production.up.railway.app',
    '127.0.0.1',
    'localhost',
]

# 🚀 Applications installées
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",  # ton app principale
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

ROOT_URLCONF = "Exemple.urls"

# 📁 Templates : utilise les templates dans chaque app (grâce à APP_DIRS)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Tu peux ajouter un dossier global ici si nécessaire
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

WSGI_APPLICATION = "Exemple.wsgi.application"

# 🗄️ Base de données SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔐 Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 Localisation
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = True

# 📂 Fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 📮 Configuration email Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'studiovisiocom@gmail.com'
EMAIL_HOST_PASSWORD = 'tgslakbqogqwrydp'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 🔐 Authentification
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/post-login/'
LOGOUT_REDIRECT_URL = '/'

# ✅ Confiance pour le CSRF en production
CSRF_TRUSTED_ORIGINS = ['https://studiovisiocom-production.up.railway.app']

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


