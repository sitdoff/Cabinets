from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "testing_db.sqlite3",
    }
}

# CACHE settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
        "TIMEOUT": 60,
    },
}

CACHE_TIMEOUT = CACHES["default"]["TIMEOUT"]
