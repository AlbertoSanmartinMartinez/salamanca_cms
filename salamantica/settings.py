#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

from decouple import config

#SECRET_KEY = 'k)y_y#@h_7mam=^^5r#09(ztwf$6&vjrf(&8w=a#!)m&i4gcg*'
SECRET_KEY = config('SECRET_KEY')

#DEBUG = True
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    '*',
]

SITE_ID = 1

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, "fixtures"),
]

# ********** MAIL SERVER CONFIG **********

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'albertosanmartinmartinez@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['MAIL_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True

# ********** SESSION CONFIG **********

LOGIN_URL = 'cms:custom_login'
LOGOUT_REDIRECT_URL = 'cms:home'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    'corsheaders',
    'widget_tweaks',
    'rest_framework',
    'generic_relations',
    'embed_video',
    'ckeditor',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'salamantica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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

"""
EMBED_VIDEO_BACKENDS = (
    'embed_video.backends.YoutubeBackend',
    'embed_video.backends.VimeoBackend',
    'embed_video.backends.SoundCloudBackend',
)
"""

WSGI_APPLICATION = 'salamantica.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

from dj_database_url import parse as dburl
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ********** STATIC FILES **********

# DEVELOPMENT

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = [
       "django.contrib.staticfiles.finders.FileSystemFinder",
       "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# ********** MEDIA FILES **********

# DEVELOPMENT

MEDIA_URL = '/media/'

MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ********** RESTFRAMEWORKS **********

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# ********** CORSEHEADERS *********

CORS_ORIGIN_ALLOW_ALL = True

# ********** BACKENDS **********

# Authentication Backends for Django and Admin
AUTHENTICATION_BACKENDS = [
    'cms.backend.CustomBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# ********** CKEDITOR CONFIG **********

CKEDITOR_UPLOAD_PATH = 'ckeditor/'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'full': {
        'toolbar': 'Full',
        'width': '100%',
        'extraPlugins': ','.join([

        ]),
        'allowedContent': True,
    },
}




#
