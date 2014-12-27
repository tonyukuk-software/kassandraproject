"""
Django settings for kassandraproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


GOOGLE_PREDICTION_PRIVATE_KEY = os.path.join(BASE_DIR, 'kassandra-bd194a2c2a59.p12')
GOOGLE_PREDICTION_PROJECT_EMAIL = '45681005892-snap58kd1fjnvu6u9eq4iml3r05rbs9q@developer.gserviceaccount.com' # REPLACE WITH YOUR PROJECT EMAIL


#Twython Constants
APP_KEY = 'eWKY4YYQdLG2zQUL0DNXyRwBX'
APP_SECRET = '4mc2U6FcCuxsqogKzJJVQNOeisNZCg48N8uoOdJZL0gxxWX5pE'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOVDbQAAAAAAx5iO14wObCejEeQ9r5itFDamj7g%3De1rg6KlOVpEtwKfx6opOGeYYQFIsgTQ7tkigBADnd99oSvbxjd'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'znj802py!=$*@26s*=gy(1vg1is5$wnlwtzzvnr7^v@qzrrq1f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'kassandra',
    'bitcoin_analyze',
    'member',
    'twython',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kassandraproject.urls'

WSGI_APPLICATION = 'kassandraproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'kassandradatabase',
          'USER': 'postgres',
          'PASSWORD': 'root',
          'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/media'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'kassandraproject/templates'),
    os.path.join(BASE_DIR, 'member/templates'),
    os.path.join(BASE_DIR, 'bitcoin_analyze/templates'),
)

#Admin Log
ADMINS = (
    ('cemkiy', 'se.cemkiy@gmail.com'),
    ('barisariburnu', 'barisariburnu@gmail.com'),)