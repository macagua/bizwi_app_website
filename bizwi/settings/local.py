from .base import  *
__author__ = 'alex'

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bizwi-demo',
        'USER': 'bizwi',
        'PASSWORD': 'bizwi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
