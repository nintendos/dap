# Django settings for dapizi project.
# -*- coding: utf-8 -*-
import os
#gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Jolly', 'jolly.jiang@sumscope.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dap',   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'iagltn',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'
DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'

CMS_LANGUAGES = {
    'default': {
        'fallbacks': ['zh-cn',],
        'redirect_on_fallback':True,
        'public': False,
        'hide_untranslated': False,
    }
}

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ("img", os.path.join(STATIC_ROOT,'img').replace('\\','/')),
    ("css",    os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ("js",     os.path.join(STATIC_ROOT,'js').replace('\\','/')),
    ("fu",     os.path.join(STATIC_ROOT,'fu').replace('\\','/')),
    )

#TinyMCE
# TINYMCE_JS_URL =("/static/js/tiny_mce/tinymce.min.js")
# TINYMCE_JS_ROOT = ("/static/js/tiny_mce")
# TINYMCE_DEFAULT_CONFIG = {
#     'plugins': "table,spellchecker,paste,searchreplace",
#     'theme': "modern",
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 10,
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-cz^0)3l^$x#*e4b!3@yck12q#186!8@ckgc=$t&f&naudbp*i'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.locale.LocaleMiddleware', 
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    #'cms.middleware.language.LanguageCookieMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'engine.MyProfile'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sumscope.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jolly.jiang@sumscope.com'
EMAIL_HOST_PASSWORD = 'art0jl'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
   os.path.join(PROJECT_PATH, "templates"),
)

# CMS_TEMPLATES = (
#       ('home.html', 'home'),
#   )

TEMPLATE_CONTEXT_PROCESSORS = (
       'django.contrib.auth.context_processors.auth',
       'django.core.context_processors.i18n',
       'django.core.context_processors.request',
       'django.core.context_processors.media',
       'django.core.context_processors.static',
       # 'cms.context_processors.media',
       # 'sekizai.context_processors.sekizai',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',
    'django.contrib.admin',
    'mptt',
    'mptt.admin',
    # 'xadmin',
    # 'crispy_forms',
    'engine',
    # 'accounts',
    'south',
    'userena',
    'userena.contrib.umessages',
    'guardian',
    'easy_thumbnails',
    # 'tinymce'
    # 'menus',
    # 'sekizai',
    # 'cms.plugins.file',  
    # 'cms.plugins.flash',  
    # #'cms.plugins.googlemap',  
    # 'cms.plugins.link',  
    # #'cms.plugins.picture',  
    # 'cms.plugins.snippet',  
    # #'cms.plugins.teaser',  
    # 'cms.plugins.text',  
    # 'cms.plugins.video',  
    #'cms.plugins.twitter',  
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
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
