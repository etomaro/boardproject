import os

SECRET_KEY = 'uyre2^mwpz98(#18gao)12gr9v77o+h$+r0jh3o2^t&curo_g5' #追加

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True