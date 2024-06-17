"""Django settings for garden project."""
import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_minio_backend',
    'rest_framework',
    'rest_framework.authtoken',
    'garden_app',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'garden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'garden.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'OPTIONS': {'options': '-c search_path=public,garden'},
        'TEST': {
            'NAME': 'test_db',
        },
    },
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

if DEBUG:
    AWS_ACCESS_KEY_ID = os.getenv('MINIO_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('MINIO_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('MINIO_STORAGE_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = os.getenv('MINIO_API')
    AWS_S3_USE_SSL = False

MINIO_ENDPOINT = 'localhost:9000'
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY_ID')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_ACCESS_KEY')
MINIO_USE_HTTPS = False
truths = ('True', 'true', '1')
MINIO_CONSISTENCY_CHECK_ON_START = os.getenv('MINIO_CONSISTENCY_CHECK_ON_START', False) in truths
MINIO_PRIVATE_BUCKETS = []
MINIO_PUBLIC_BUCKETS = [
    'images',
]
