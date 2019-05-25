import os
import pymysql
import django_smtp_ssl

pymysql.install_as_MySQLdb()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
with open('secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '.dusaiphoto.com', '.dusai.net']

# Application definition

INSTALLED_APPS = [
    # admin增强
    'jet.dashboard',
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'userinfo',
    'article',  # 文章
    'comments',  # 评论
    'album',  # 相册
    'course',  # 教程
    'readbook',  # 读书
    'imagesource',  # 图库
    'vlog',  # 视频
    'aboutme',  # 作者
    'extends',

    'utils',  # 工具

    # django-allauth
    # 必须安装的app
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 下面是第三方账号相关的，选了weibo和github
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github',

    # 标签
    'taggit',

    # mptt
    'mptt',

    # notifications
    'notifications',
    'mynotifications',

    # haystack search
    'haystack',

    # 富文本编辑器
    'ckeditor',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # cor-headers
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dusainet2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'dusainet2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# 开发数据库

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    with open('mysql_key.txt') as f:
        MYSQL_PASSWORD = f.read().strip()
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dusainet2',
            'USER': 'root',
            'PASSWORD': MYSQL_PASSWORD,
            'HOST': '127.0.0.1',
            'PORT': '3306',
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

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'nginx_static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# django-allauth相关设置
AUTHENTICATION_BACKENDS = (
    # django admin所使用的用户登录与django-allauth无关
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

# Email setting
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# SMTP服务器，我使用的是sendclound的服务
EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = 'dusaiphoto@foxmail.com'
with open('email_host_password.txt') as f:
    EMAIL_HOST_PASSWORD = f.read().strip()
EMAIL_PORT = 465

# 是否使用了SSL 或者TLS
# EMAIL_USE_SSL = True
EMAIL_USE_TLS = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost
DEFAULT_FROM_EMAIL = '杜赛的个人网站 <dusaiphoto@foxmail.com>'
# LOGIN_REDIRECT_URL = '/account/weibo_login_success/'
LOGIN_REDIRECT_URL = '/'

# django的评论库是一个站点，所以需要添加sites的应用并设置当前django工程的站点id=1
SITE_ID = 1

# haystack相关配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'article.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

CORS_ORIGIN_ALLOW_ALL = True

# ckeditor
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用配置
    'default': {
        'language': 'zh-hans',
        'width': 'auto',
        'height': '250px',
        'tabSpaces': 4,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Smiley', 'CodeSnippet', '-', 'Bold', 'Italic', 'Underline', 'RemoveFormat', ],
            ['NumberedList', 'BulletedList'],
            ['TextColor', 'BGColor'],
            ['Link', 'Unlink'],
            ['Undo', 'Redo', 'Marker'],
            ['Maximize']
        ],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils', ]),
    }
}
