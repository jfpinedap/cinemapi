from .base import *
from .base import env



READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR.path(".envs/.develop")))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="simeit62zrwfvxr!x5_x6f*7ie+ds(-ha1rm!v6kq)kg4tt4jqy)+=trik",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["ec2-52-90-243-117.compute-1.amazonaws.com"])
HOST_URL = 'http://ec2-52-90-243-117.compute-1.amazonaws.com'

# logging config
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'development_logfile': {
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'logs/{0}.log'.format(datetime.datetime.now().strftime("%m-%d-%Y")),
            'formatter': 'verbose'
        },
        'production_logfile': {
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/{0}.log'.format(datetime.datetime.now().strftime("%m-%d-%Y")),
            'maxBytes': 1024 * 1024 * 100,  # 100MB
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'dba_logfile': {
            'filters': ['require_debug_false', 'require_debug_true'],
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'logs/{0}.log'.format(datetime.datetime.now().strftime("%m-%d-%Y")),
            'formatter': 'verbose'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'loggers': {
        'coffeehouse': {
            'handlers': ['development_logfile', 'production_logfile', 'dba_logfile'],
        },
        'dba': {
            'handlers': ['dba_logfile', 'dba_logfile', 'production_logfile'],
        },
        'django': {
            'handlers': ['development_logfile', 'production_logfile', 'dba_logfile'],
        },
        'py.warnings': {
            'handlers': ['development_logfile', 'dba_logfile', 'production_logfile'],
        },
    }
}

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.int('POSTGRES_PORT'),
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
