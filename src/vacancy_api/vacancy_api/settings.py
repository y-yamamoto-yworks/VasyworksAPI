"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '任意のキー'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'building',
    'company',
    'data_link',
    'documents',
    'master',
    'rent_db',
    'room',
    'search',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vacancy_api.urls'

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

WSGI_APPLICATION = 'vacancy_api.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rent_db',
        'USER': 'yworks',
        'PASSWORD': '任意のパスワード',
        'HOST': 'DBサーバのIPアドレスなど',
        'PORT': '5432',
    }
}


# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    # 公開用
    # 'https://vasyworks-api.yworks.hogehoge.net',
    # 'http://vasyworks-api.yworks.hogehoge.net',

    # 開発用
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]


# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    # 本番用
    # 'https://vasyworks-api.hogehoge.net',
    # 'http://vasyworks-api.hogehoge.net',

    # 開発用
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
CORS_PREFLIGHT_MAX_AGE = 60 * 30  # 許可時間30分


# Password validation

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Humanize
NUMBER_GROUPING = 3


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.ListApiPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Application settings
BASE_URL = 'http://127.0.0.1:8000/'    # APIのベースURL
COMPANY_ID = 1      # 会社ID（会社マスタ参照用）
CONDO_FEES_NAME = '共益費'         # 共益費項目の表示名（共益費または管理費）
CACHE_FILE_URL = '/static/cache/'       # キャッシュファイルのURL
CACHE_FILE_DIR = os.path.join(BASE_DIR, 'static', 'cache')      # キャッシュファイルのディレクトリ
ORIGINAL_FILE_DIR = os.path.join(BASE_DIR, 'media', 'public')       # オリジナルファイルのディレクトリ
WATER_MARK_FONT_SIZE = 32   # キャッシュ画像の透かしのフォントサイズ
WATER_MARK_OPACITY = 64     # キャッシュ画像の透かしの不透明度
THUMBNAIL_IMAGE_SIZE = 240      # サムネイルキャッシュ画像の最大サイズ
SMALL_IMAGE_SIZE = 320      # 小キャッシュ画像の最大サイズ
MEDIUM_IMAGE_SIZE = 640     # 中キャッシュ画像の最大サイズ
LARGE_IMAGE_SIZE = 1280     # 大キャッシュ画像の最大サイズ
