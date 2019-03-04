# Database configuration
from .settings import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('USERNAME'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOSTNAME'),
        'PORT': os.environ.get('PORT'),
    }
}