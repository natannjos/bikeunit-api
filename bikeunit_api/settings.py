import os
import environ

root = environ.Path(__file__) - 2  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)  # set default values and casting
# environ.Env.read_env()  # reading .env file
environ.Env.read_env('%s/.env' % root)  # reading .env file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = root()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # apps
    'grupos',
    'usuarios',
    'core_auth',

    # libs
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',

    'rest_auth',
    'rest_auth.registration',

    'allauth',
    'allauth.account',

    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django_filters',

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
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3333',
)

ROOT_URLCONF = 'bikeunit_api.urls'

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
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'bikeunit_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db(),
    'extra': env.db('SQLITE_URL', default='sqlite:///db.sqlite3')
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Redefine "/admin" URI ot admin panel in ".env" file if you need
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')


# django-cors-headers settings
# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = env.tuple('CORS_ORIGIN_WHITELIST')


EMAIL_CONFIG = env.email_url('EMAIL_URL', default='consolemail://')
vars().update(EMAIL_CONFIG)
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL',
                   default=EMAIL_CONFIG['EMAIL_HOST_USER'])
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default=EMAIL_CONFIG['EMAIL_HOST_USER'])


# django-rest-auth settings
# https://django-rest-auth.readthedocs.io/en/latest/configuration.html
REST_SESSION_LOGIN = True
SITE_ID = env('SITE_ID')


# django-allauth settings
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# for the correct link in the account confirmation email
ACCOUNT_ADAPTER = 'core_auth.adapter.CustomAccountAdapter'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = env(
    'ACCOUNT_AUTHENTICATION_METHOD', default='username_email')
# ACCOUNT_EMAIL_VERIFICATION = 'optional'  # user will login automaticly after registration
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # user can't login until confirm the account
ACCOUNT_EMAIL_VERIFICATION = env(
    'ACCOUNT_EMAIL_VERIFICATION', default='mandatory')
ACCOUNT_LOGOUT_ON_GET = True
CONFIRM_EMAIL_ON_GET = True
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
# ACCOUNT_EMAIL_SUBJECT_PREFIX (=”[Site] ”)
# Subject-line prefix to use for email messages sent. By default, the name of the current Site (django.contrib.sites) is used.
# ACCOUNT_DEFAULT_HTTP_PROTOCOL (=”http”)
# The default protocol used for when generating URLs, e.g. for the password forgotten procedure. Note that this is a default only – see the section on HTTPS for more information.


# DRF settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'core_auth.custom_auth.CustomTokenAuthentication',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': env.int('PAGE_SIZE', default=5),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)

}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'core_auth.serializers.UserSerializer',
    'PASSWORD_RESET_SERIALIZER': 'core_auth.serializers.CustomPasswordResetSerializer',
}


# Customizing user model
# https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'core_auth.User'


# https://docs.djangoproject.com/en/2.1/ref/settings/#authentication-backends
# https://django-allauth.readthedocs.io/en/latest/installation.html
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
