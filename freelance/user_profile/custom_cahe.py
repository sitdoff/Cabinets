from functools import wraps

from django.core.cache import cache
from django.views.decorators.cache import cache_page


def cache_user_profile(timeout):
    """
    Used to ensure that each user has a unique cache profile.
    """

    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            cache_key = f"{request.path}-{request.user.id}"
            response = cache.get(cache_key)
            if not response:
                response = view(request, *args, **kwargs)
                cache.set(cache_key, response, timeout)
            return response

        return _wrapped_view

    return decorator
