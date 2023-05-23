import dj_database_url
import os

INSTALLED_APPS = [
    # other apps
    'bingapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('/BINGPROJECT', 'static')  # Set the static root directory

SECRET_KEY = 'fr_m*t!f#kgqks0k@bdggb-9%^cbr!*@+-q2m&$+g84x0p814m'

os.environ['DATABASE_URL'] = 'postgres://botdb_d97h_user:oKU64c7jPkwVkqULssNdbphwVoMziUCS@dpg-chm3psg2qv27ib3rj31g-a.singapore-postgres.render.com/botdb_d97h'
DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']
DEBUG = True
ROOT_URLCONF = 'bingproject.urls'
