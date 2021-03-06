import os
import chishop
from chishop.conf.default import *

DEBUG = True
TEMPLATE_DEBUG = True

TIME_ZONE = 'America/New_York'

DATABASES = dict(
	default = dict(
		ENGINE = 'django.db.backends.postgresql_psycopg2',
		NAME = 'chishop',
		USER = 'chishop',
		PASSWORD = 'GogDadjerm1',
		HOST = 'localhost',
		PORT = '',
	)
)

STATIC_URL = '/media/'

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'chishop.search_sites'
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(chishop.__file__), 'haystack')
DJANGOPYPI_PROXY_MISSING = True
CACHE_PROXIED_PACKAGES = True
