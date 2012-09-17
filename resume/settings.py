# Django settings for resume project.

import os

from lib.S3 import CallingFormat
import dj_database_url

SITE_ROOT = os.path.abspath(os.path.dirname(__file__))


#DEBUG_TOOLBAR_CONFIG[INTERCEPT_REDIRECT] = False
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

ADMINS = (
     ('David Y. Kay', 'davidykay@gmail.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

if os.environ.get('ENVIRONMENT') == 'production':
  DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
  # TODO: Debug only!
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'resume',         # Or path to database file if using sqlite3.
          'USER': '',                      # Not used with sqlite3.
          'PASSWORD': '',                  # Not used with sqlite3.
          'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
      }
  }


  MEDIA_ROOT  = 'media/'
  STATIC_ROOT = ''

  MEDIA_URL  = 'http://media.davidykay.com/media/'
  STATIC_URL = 'http://media.davidykay.com/'

  AWS_BUCKET_NAME = 'media.davidykay.com'   # Bucket name
  # BOTO
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
  AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
  AWS_STORAGE_BUCKET_NAME = AWS_BUCKET_NAME
else:
  DEBUG = True
  TEMPLATE_DEBUG = DEBUG

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'resume',         # Or path to database file if using sqlite3.
          'USER': '',                      # Not used with sqlite3.
          'PASSWORD': '',                  # Not used with sqlite3.
          'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
      }
  }

  STATIC_ROOT = SITE_ROOT + '/static/'
  STATIC_URL = '/static/'
  # Absolute filesystem path to the directory that will hold user-uploaded files.
  # Example: "/home/media/media.lawrence.com/media/"
  #MEDIA_ROOT = ''
  MEDIA_ROOT = SITE_ROOT + '/media/'

  # URL that handles the media served from MEDIA_ROOT. Make sure to use a
  # trailing slash.
  # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
  MEDIA_URL = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    SITE_ROOT + '/static_storage/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yy8gwm7u+=q_=kldte)n&amp;d8qxwx4+*e_15ku()=x&amp;lch#2wg8)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    # added by us
    'django.core.context_processors.request',
    # default
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)


MIDDLEWARE_CLASSES = (
# django middleware
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 3rd party
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'resume.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'resume.wsgi.application'

TEMPLATE_DIRS = (
    SITE_ROOT + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )


EMBEDLY_KEY = '489ce883805046549cce73eccf0bb270'


INSTALLED_APPS = (
    # our app
    'resume.gigs',

    # 3rd party
    #'boto',
    'embeds',
    'south',
    'debug_toolbar',

    # django
    'django.contrib.markup',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)


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
