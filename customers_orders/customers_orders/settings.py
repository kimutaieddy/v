"""


This module contains the settings for the customers_orders project, including
configuration for installed applications, middleware, templates, database, 
authentication, internationalization, static files, and third-party integrations.

Attributes:
    BASE_DIR (Path): The base directory of the project.
    SECRET_KEY (str): The secret key for the Django project.
    DEBUG (bool): Flag indicating whether debug mode is enabled.
    ALLOWED_HOSTS (list): List of allowed hostnames.
    INSTALLED_APPS (list): List of installed applications.
    MIDDLEWARE (list): List of middleware components.
    ROOT_URLCONF (str): The root URL configuration module.
    TEMPLATES (list): List of template configurations.
    WSGI_APPLICATION (str): The WSGI application module.
    DATABASES (dict): Database configuration.
    AUTH_PASSWORD_VALIDATORS (list): List of password validators.
    LANGUAGE_CODE (str): The default language code.
    TIME_ZONE (str): The default time zone.
    USE_I18N (bool): Flag indicating whether internationalization is enabled.
    USE_TZ (bool): Flag indicating whether timezone support is enabled.
    STATIC_URL (str): URL for serving static files.
    DEFAULT_AUTO_FIELD (str): Default primary key field type.
    REST_FRAMEWORK (dict): Django REST framework configuration.
    SITE_ID (int): Site ID for django.contrib.sites.
    OIDC_RP_CLIENT_ID (str): OIDC client ID.
    OIDC_RP_CLIENT_SECRET (str): OIDC client secret.
    OIDC_OP_AUTHORIZATION_ENDPOINT (str): OIDC authorization endpoint.
    OIDC_OP_TOKEN_ENDPOINT (str): OIDC token endpoint.
    OIDC_OP_USER_ENDPOINT (str): OIDC user info endpoint.
    OIDC_RP_SIGN_ALGO (str): OIDC signing algorithm.
    LOGIN_REDIRECT_URL (str): URL to redirect to after login.
    AUTHENTICATION_BACKENDS (tuple): Tuple of authentication backends.
    AFRICASTALKING_USERNAME (str): Username for Africa's Talking API.
    AFRICASTALKING_API_KEY (str): API key for Africa's Talking API.
    TESTING (bool): Flag indicating whether tests are being run.
Django settings for customers_orders project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k6*)^@o=t+eviu_h-)sqn5azmjomg9ymbxv!p_2zu(dgv2t4@h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# Assuming the internal organization-specific modules are used, the INSTALLED_APPS list should remain the same as in the retrieved context.
# Make sure to add the relevant imports for internal organization modules, packages, and libraries.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    "django.contrib.sites",
    'mozilla_django_oidc',
    'rest_framework.authtoken',
    'corsheaders',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
]

ROOT_URLCONF = 'customers_orders.urls'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

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

WSGI_APPLICATION = 'customers_orders.wsgi.application' #


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'starry_night',
        'USER': 'galactic_hiker',
        'PASSWORD': 'Nebula$2024!',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',  # Enables basic username/password authentication
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Ensures that only authenticated users can access the API
    ],
}
#site id for django-oidc eeded for django.contrib.sites 
SITE_ID = 1

#OIDC settings
OIDC_RP_CLIENT_ID = '1234567890-abcdefghij.apps.googleusercontent.com'
OIDC_RP_CLIENT_SECRET = 'ABCDEF1234567890GHIJKLMNOPQRSTUVWXYZ'
OIDC_OP_AUTHORIZATION_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth'
OIDC_OP_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
OIDC_OP_USER_ENDPOINT = 'https://openidconnect.googleapis.com/v1/userinfo'

OIDC_RP_SIGN_ALGO = 'RS256'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)



AFRICASTALKING_USERNAME = 'your-username' 
AFRICASTALKING_API_KEY = 'atsk_2b6de0807d0ff2fd13f6e7c454b962e056120738023827b4625156a209b6b5e725b40650'


#Test mode flag to determine if the application is running in test mode (Just for the tests)
import sys

# Determine if the application is running in test mode
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# Adjust authentication backends based on the environment
if TESTING:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',  
    )
else:
    AUTHENTICATION_BACKENDS = (
        'mozilla_django_oidc.auth.OIDCAuthenticationBackend', 
    )
