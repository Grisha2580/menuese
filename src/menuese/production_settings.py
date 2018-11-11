import os

"""
Django settings for menuese project.

Generated by 'django-admin startproject' using Django 2.0.5.

"""

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

SECRET_KEY = ''
# MYSQL_PASSWORD = ''
with open( '/home/grython/menuese/secret_key.txt' ) as f:
	SECRET_KEY = f.read().strip()
with open( '/home/grython/menuese/mysql_password.txt' ) as f:
	MYSQL_PASSWORD = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['grython.pythonanywhere.com', 'https://www.pythonanywhere.com', 'pythonanywhere.com']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework.authtoken',
	'rest_auth',
	'django_filters',
	'restaurants',
	'menu',
	'orders',
	'users',
]

REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
		'rest_framework.renderers.BrowsableAPIRenderer',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
	),
	'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

REST_AUTH_SERIALIZERS = {
	'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',
	'USER_DETAILS_SERIALIZER': 'users.serializers.CustomUserSerializer',
}

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'menuese.urls'
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

ADMIN_SITE_HEADER = "MENUESE ADMINISTRATION"

WSGI_APPLICATION = 'menuese.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'OPTIONS': {
# 			'read_default_file': '/home/grython/my.cnf',
# 		},
# 		'NAME': 'grython$menuesemysql',
# 		'USER': 'grython',
# 		'PASSWORD': MYSQL_PASSWORD,
# 		'HOST': 'grython.mysql.pythonanywhere-services.com',
# 		'TEST': {
# 			'NAME': 'grython$_menuesemysql',
# 		},
# 	}
# }
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join( BASE_DIR, 'db.sqlite3' ),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join( BASE_DIR, 'static' )

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
