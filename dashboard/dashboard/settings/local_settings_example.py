import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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

PRODUCTION = False
SITE_URL = "127.0.0.1:8000"

DEBUG = True
ALLOWED_HOSTS = ["*"]

EMAIL_INFO = ''


# to local_settings ( in the future)

URL_CORE = "http://127.0.0.1:8001"
URL_API_V1 = URL_CORE + '/api/v1/'

APP_RELEASE = ""
APP_OWNER = 'Bizwi'
APP_NAME = 'Retail Analytics'