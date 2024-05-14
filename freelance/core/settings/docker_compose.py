from core.settings.base import *

print("-" * 50)
print("WARNING! DOCKER COMPOSE SETTINGS!")
print("-" * 50)

# For django_gebug_toolbar
if DEBUG:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
