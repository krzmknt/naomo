""" Django settings for naomo project.  Generated by 'django-admin startproject' using Django 2.0.3.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json
import traceback

# ログ出力で仕様するハンドラを指定する
LOG_HANDLER = ["app"]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ekf!&30u3&idt-qr3250(t+j#%@(vyxr02c-7fj!a81$!)#q=('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 接続を許可するサーバのIPやドメインを設定する
# 何も設定していない場合は、ローカルホスト(localhost)からの接続のみ可能な状態
ALLOWED_HOSTS = [
    "localhost",
    "krzmknt.com",
    "52.199.251.130"
]

# Application definition
# 「app」を追加。これを追加しないとtemplatetagsに定義したカスタムタグが認識されない
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

ROOT_URLCONF = 'naomo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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



WSGI_APPLICATION = 'naomo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'naomo',
        'USER': 'root',
        'PASSWORD': 'krzmknt',
        'HOST': '172,23,0.6',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

# collectstatic collect to this dir
STATIC_ROOT = os.path.join(BASE_DIR,"static")

# collectstatic collect from this dirs
STATICFILE_DIRS = {
}


LOGGING = {
    'version': 1,
    'formatters': {
        'app': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        }
    },
    'handlers': {
        'app': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/home/work/django/app.log',
            'formatter': 'app',
            'when': 'D',        # 単位 Dは日
            'interval': 1,      # 何日おきか指定
            'backupCount': 30,  # バックアップ世代数
        }
    },
    'loggers': {
        'django': {
            'handlers': ['app'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['app'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'app': {
            'handlers': LOG_HANDLER,
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# セッションエンジンの設定
# cookieを用いたセッションを使用する
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# ログイン状態の有効期限（秒）
# ここに指定した有効期限（秒）を超えるまでログイン状態を保つ事ができる
# セッション自体の有効期限はSESSION_COOKIE_AGE
# 8h * 60m * 60s
LOGIN_LIMIT = 28800

# セッションの有効期間(秒)
# 利用者毎にセッション有効期間を変えたい場合は、request.session.set_expiry(value)を用いる
SESSION_COOKIE_AGE = 1800
