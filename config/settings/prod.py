from .base import *  # noqa

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vmails',
        'USER': 'mailwriter',
        'HOST': '127.0.0.1',
        'PORT': get_secret('DB_PORT'),
        'PASSWORD': get_secret('DB_PASS'),
    }
}

ALLOWED_HOSTS = [
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'http://vmail-admin.vpn.dominowisla.pl',
    'http://vmails.vpn.dominowisla.pl',
]
