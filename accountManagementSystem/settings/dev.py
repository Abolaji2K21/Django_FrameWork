from .general import *

SECRET_KEY = 'django-insecure-h-2)+p87-xvo(m+yz!n1kt^74mcyp=utv$=^w&=vyl1)zge7r*'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'account_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = "info@agudabank.com"
