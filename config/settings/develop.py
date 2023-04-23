from config.settings import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.develop.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['file'],
    },
    'formatters': {
        'verbose': {
            'format': (
                '%(asctime)s %(levelname)s %(name)s %(message)s'
                ' [PID:%(process)d:%(threadName)s]')},
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, LOG_FILENAME),
            'maxBytes': 10*1024*1024,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}