"""
Django settings for 50shades project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

from configurations import Configuration, values


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Common(Configuration):
    DJANGO_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # 'django.contrib.sites',
        # Useful template tags
        # 'django.contrib.humanize',
        # Admin
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
    )

    THIRD_PARTY_APPS = (
        'south',
    )

    LOCAL_APPS = (
        'apps.core',
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    )

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    ADMINS = (
        ('Juan Riaza', 'hi@juanriaza.com'),
    )
    MANAGERS = ADMINS

    SITE_ID = 1
    ROOT_URLCONF = 'conf.urls'
    WSGI_APPLICATION = 'conf.wsgi.application'
    SECRET_KEY = 'not-so-secret'

    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    DATABASES = values.DatabaseURLValue(
        'postgres://localhost/50shades')
    CACHES = values.CacheURLValue(
        default='locmem://50shades')

    FIXTURE_DIRS = (
        os.path.join(BASE_DIR, 'fixtures'),
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates_common'),
    )

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static_common'),
    )

    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }


class Local(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)

    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = values.DatabaseURLValue(
        'sqlite:////%s' % os.path.join(BASE_DIR, '50shades.sqlite'))


class Production(Common):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    SECRET_KEY = values.SecretValue()

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'djangosecure',
        'gunicorn',
    )

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + (
        'djangosecure.middleware.SecurityMiddleware',
    )

    ALLOWED_HOSTS = ['*']

    SECURE_BROWSER_XSS_FILTER = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
