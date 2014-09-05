import os

import django

DEBUG = True

PROJECT_DIR = os.path.dirname(__file__)

STATIC_URL = PROJECT_DIR + '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb',
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'report_builder',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

if django.VERSION[0] == 1 and django.VERSION[1] < 7:
    INSTALLED_APPS += ('south',)

ROOT_URLCONF = "test_urls"

SECRET_KEY = 'foo'

SITE_ID = 1

SOUTH_TESTS_MIGRATE = False
