"""
Django settings for erehwon project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
SECRET_KEY = os.environ["SECRET_KEY"]


ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = '/home'


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'profiles',
    'custom_user',
    'erehwon',
    'messagesApp',
    'postman',
    'ajax_select',
    'notifications',
]

SITE_ID = 1
# POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
# POSTMAN_DISALLOW_MULTIRECIPIENTS = True  # default is False
# POSTMAN_DISALLOW_COPIES_ON_REPLY = True  # default is False
# POSTMAN_DISABLE_USER_EMAILING = True  # default is False
POSTMAN_AUTO_MODERATE_AS = True  # default is None
# POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
POSTMAN_NAME_USER_AS = 'username'   #default is None
# POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
POSTMAN_NOTIFIER_APP = "messagesApp"  # default is 'notification'
# POSTMAN_MAILER_APP = None  # default is 'mailer'
# POSTMAN_AUTOCOMPLETER_APP = {
# 'name': '',  # default is 'ajax_select'
# 'field': '',  # default is 'AutoCompleteField'
# 'arg_name': '',  # default is 'channel'
# 'arg_default': 'postman_friends',  # no default, mandatory to enable the feature
# }  # default is {}



MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'erehwon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(BASE_DIR, 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'erehwon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',# Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'erehwon',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

AUTH_USER_MODEL = 'profiles.ErehwonUser'

CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
]

# Registration settings using sendgrid

ACCOUNT_ACTIVATION_DAYS = 7
EXPIRATION_DAYS = 5
REGISTRATION_DEFAULT_FROM_EMAIL = "projecterehwon@gmail.com"
REGISTRATION_EMAIL_HTML = True
REGISTRATION_AUTO_LOGIN = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
