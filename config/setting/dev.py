from config.settings import *
from secretvariables import secret_key

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', ]

# INSTALLED_APPS = []

# sites framework
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

CSRF_COOKIE_SECURE = False

MAINTENANCE_MODE = False

COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True

if not COMPRESS_ENABLED:
    COMPRESS_ENABLED = True
    COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
    COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]