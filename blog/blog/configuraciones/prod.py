from ..settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_NAME="Informatorio"

ALLOWED_HOSTS = ['grupo1comision2info.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyecto',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='grupo1.informatorio.2023@gmail.com'
EMAIL_HOST_PASSWORD =''#sacado temporalmente
EMAIL_USE_TLS = True