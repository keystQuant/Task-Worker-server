import os
import raven

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '!n0+=qj9f+yuw1qqu5majpga*i1o%lg)bh8k&b6ig)+b)k@oi5'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '127.0.1.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # corsheaders
    'corsheaders',

    # Sentry: 에러 로깅
    'raven.contrib.django.raven_compat',

    # Django Restframework (API Template)
    'rest_framework',

    # celery + celerybeat
    'django_celery_beat',
    'django_celery_results',

    # 몰레큘러 앱 정의내리는 곳
    'tasks',
]

### Sentry 새팅 ###
RAVEN_CONFIG = {
    'dsn': 'https://46ff90ce43684e15b6d5dc6e7aad4925:4c93eef751b24ee0b4d9afb1641f432c@sentry.io/1274804',
    'release': raven.fetch_git_sha(BASE_DIR),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'keystone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'keystone.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'keystone',
        'USER': 'keystone',
        'PASSWORD': 'keystoneinvestmentpostgresql2018',
        'HOST': os.environ.get('PG_HOST', 'db'),
        'PORT': 5432,
    },
} # --> 도커 컨테이너인 'db'가 제대로 인식되지 않음

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


LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True # 외부에서 API 요청 가능하도록 새팅

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://redis:6379/',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'PASSWORD': 'keystoneredisadmin2018'
        }
    }
}

amqp_user = 'admin'
amqp_pass = 'keystonerabbitadmin2018'
amqp_url = 'amqp://{}:{}@rabbit:5672//'.format(amqp_user, amqp_pass)

CELERY_BROKER_URL = amqp_url
CELERY_RESULT_BACKEND = 'django-db' # https://github.com/celery/django-celery-results/issues/19
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = False
