from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^fa&ks2)bze(&i8+-)ajv5^&-^ndum55f&q2whmg_%^x&4i+ad'

DEBUG = True

ALLOWED_HOSTS = ['test.it-kyzyl.ru', '192.168.1.253', '127.0.0.1']
#ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    #'image_uploader_widget',
    'rest_framework',
    'django_rq',

    'mainapp',
    'userapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'pg': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uch',
        'USER': 'user',
        'PASSWORD': 'user123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_USER_IMAGE = MEDIA_URL + 'user/nophoto.png'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ['https://test.it-kyzyl.ru', 'http://localhost']
#CSRF_TRUSTED_ORIGINS = ['http://localhost']

AUTH_USER_MODEL = 'userapp.ScUser'
LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/user/profile/'
LOGOUT_REDIRECT_URL = '/'

INTERNAL_IPS = [
    "192.168.1.253",
    "127.0.0.1",
]

#SHOW_TOOLBAR_CALLBACK = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny' #DjangoModelPermissionsOrAnonReadOnly'
    ]
}

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        #'USERNAME': 'some-user',
        #'PASSWORD': 'some-password',
        #'DEFAULT_TIMEOUT': 360,
        #'REDIS_CLIENT_KWARGS': {    # Eventual additional Redis connection arguments
        #    'ssl_cert_reqs': None,
        #},
    },
}

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# тестовая отправка писем. сохраняем их в папке emails
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend' 
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')
# отправка почты
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025 
EMAIL_HOST_USER = '' 
EMAIL_HOST_PASSWORD =  '' 
EMAIL_USE_TLS = False 

DEFAULT_FROM_EMAIL = 'robot@superschool.ru'
SERVER_EMAIL = 'robot@superschool.ru'
EMAIL_ADMIN = 'mistrikov1@yandex.ru'
ADMINS = [('Игорь', 'mistrikov1@yandex.ru')]

