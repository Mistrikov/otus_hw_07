from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^fa&ks2)bze(&i8+-)ajv5^&-^ndum55f&q2whmg_%^x&4i+ad'

# DEBUG = True

# ALLOWED_HOSTS = ['test.it-kyzyl.ru', '192.168.1.253', '127.0.0.1', 'sc.it-kyzyl.ru', 'localhost', '10.8.0.9']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    # 'image_uploader_widget',
    'rest_framework',
    'django_rq',
    # 'rest_framework.authtoken',
    'django_filters',
    'rest_framework_simplejwt',
    'graphene_django',
    'corsheaders',

    'mainapp',
    'userapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'corsheaders.middleware.CorsMiddleware',
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

# DATABASES = {
#    'default1': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    },
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'uch',
#        'USER': 'user',
#        'PASSWORD': 'user123',
#        'HOST': 'pg',
#        'PORT': '5432',
#    }
# }


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

# CSRF_TRUSTED_ORIGINS = ['https://test.it-kyzyl.ru', 'http://localhost', 'https://sc.it-kyzyl.ru']

AUTH_USER_MODEL = 'userapp.ScUser'
LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/myedu/list/'  # '/user/profile/'
LOGOUT_REDIRECT_URL = '/'

INTERNAL_IPS = [
    "192.168.1.253",
    "127.0.0.1",
]

# SHOW_TOOLBAR_CALLBACK = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

DEFAULT_CHARSET = 'utf8'
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


# отправка почты
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'robot@superschool.ru'
SERVER_EMAIL = 'robot@superschool.ru'
EMAIL_ADMIN = 'mistrikov1@yandex.ru'
ADMINS = [('Игорь', 'mistrikov1@yandex.ru')]

GRAPHENE = {
    "SCHEMA": "api.schema.schema"  # приложение.файл.класс_схемы
}

# MIDDLEWARE_CLASSES = (
#    'corsheaders.middleware.CorsMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    )

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = ['http://localhost:8000', 'https://test.it-kyzyl.ru', 'http://192.168.1.253:8000']

print("load base_settings file")
