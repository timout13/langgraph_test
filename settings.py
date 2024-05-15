__import__('pysqlite3')
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
