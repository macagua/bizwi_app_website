import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = BASE_DIR + '/Core/static/'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bizwi',                      # Or path to database file if using sqlite3.
        'USER': 'bizwi',                      # Not used with sqlite3.
        'PASSWORD': 'bizwi',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',
    }
}

APP_OWNER = "BIZWI"
APP_NAME = "BIZWI"

PRODUCTION = False
SITE_URL = "127.0.0.1:8000"

DEBUG = True
ALLOWED_HOSTS = ["*"]

EMAIL_INFO = ''