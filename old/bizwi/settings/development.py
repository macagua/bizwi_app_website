from .base import *
__author__ = 'alex'

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bizwi_demo',
        'USER': 'alex',
        'PASSWORD': '20643647',
        'HOST': '52.18.184.65',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'
