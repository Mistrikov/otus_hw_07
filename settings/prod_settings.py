import os
from pathlib import Path
from .base_settings import * # NOQA

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ['localhost', '192.168.1.253', '10.8.0.9', '10.8.0.1', 'test.it-kyzyl.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'pg',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_USER_IMAGE = MEDIA_URL + 'user/nophoto.png'

CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://10.8.0.9', 'http://192.168.1.253', 'https://test.it-kyzyl.ru']

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost"
]

RQ_QUEUES = {
    'default': {
        'HOST': 'redishost',
        'PORT': 6379,
        'DB': 0,
        # 'USERNAME': 'some-user',
        # 'PASSWORD': 'some-password',
        # 'DEFAULT_TIMEOUT': 360,
        # 'REDIS_CLIENT_KWARGS': {    # Eventual additional Redis connection arguments
        #    'ssl_cert_reqs': None,
        # },
    },
}

CELERY_BROKER_URL = "redis://redishost:6379/0"
CELERY_RESULT_BACKEND = "redis://redishost:6379/0"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ['http://localhost:8001', 'http://game.it-kyzyl.ru:8001', 'http://10.8.0.1:8001']

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = ['http://localhost:8081', 'https://test.it-kyzyl.ru']

print("load prod_settings file")
