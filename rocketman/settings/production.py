from django.conf.global_settings import ALLOWED_HOSTS, SECRET_KEY
from .base import *

DEBUG = False
SECRET_KEY = ''
ALLOWED_HOSTS = ['localhost', 'rocketman.banana.com', '*']


cwd = os.getcwd()
CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": f"{cwd}/.cache",
            }
        }

DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.postgresql_psycopgq2',
            "NAME": 'rocketman',
            "USER": 'rocketman',
            "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx2',
            "HOST": 'localhost',
            "PORT": "",
        }
}

try:
    from .local import *
except ImportError:
    pass

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://c47ab77b314144abacf6218125ef8c30@o1361469.ingest.sentry.io/6650140",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
