"""
Django settings for EXAMPLE project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "pi!!eb6ym55$q)cy14k0c32svx#7(d=&_n&&=**8(3)avkirq$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EXAMPLE = "staggered"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "plata",
    "plata.contact",
    "plata.discount",
    "plata.payment",
    "plata.product",
    "plata.shop",
    EXAMPLE,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "%s.urls" % EXAMPLE

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "plata.context_processors.plata_context",
            ]
        },
    }
]

WSGI_APPLICATION = "%s.wsgi.application" % EXAMPLE


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "%s.sqlite3" % EXAMPLE),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "de-ch"

TIME_ZONE = "Europe/Zurich"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"

# ## PLATA settings

# PLATA_PRICE_INCLUDES_TAX = False

POSTFINANCE = {
    "PSPID": "plataTEST",
    "SHA1_IN": "plataSHA1_IN",
    "SHA1_OUT": "plataSHA1_OUT",
    "LIVE": False,
}

PAYPAL = {"BUSINESS": "example@paypal.com", "LIVE": False}

PLATA_REPORTING_ADDRESSLINE = "Example Corp. - 3. Example Street - 1234 Example"

PLATA_SHOP_PRODUCT = "%s.Product" % EXAMPLE
CURRENCIES = ("EUR", "CHF", "USD")

TEST_RUNNER = "options.test_utils.test_runner_with_coverage"
COVERAGE_MODULES = ["plata"]
