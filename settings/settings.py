import os
from pathlib import Path
from .base_settings import * # NOQA

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ['*']  # ['127.0.0.1', 'localhost', '192.168.1.253']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CSRF_TRUSTED_ORIGINS = ['http://localhost', 'https://test.it-kyzyl.ru']

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost"
]

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
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

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ['http://localhost:8000', 'http://localhost:8081']

# тестовая отправка писем. сохраняем их в папке emails
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')

EMAIL_ADMIN = 'mistrikov1@yandex.ru'

print("load settings file")
