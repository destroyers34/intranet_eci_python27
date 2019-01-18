from os.path import join, dirname, normpath

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'intranetdjangodev',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'Dkh8c922ht',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'default-character-set': 'utf8',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-z8cn559pfn#kk05q%ro=7*6#0^j!t3qcsql_q4rh&amp;#9o=5@rp'

# Used to provide absolute paths.  Normally the default is fine.
LOCAL_PATH = normpath(join(dirname(__file__), '..'))

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
#	'admineugenie.webfactional.com',
]

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'intranet.wsgi_prod.application'

DEBUG = True

GRAPPELLI_SWITCH_USER = True
