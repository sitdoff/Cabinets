from core.settings.settings import *

# For django_gebug_toolbar
INTERNAL_IPS = ["127.0.0.1"]

# CACHE settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
        "TIMEOUT": 60,
    },
}
