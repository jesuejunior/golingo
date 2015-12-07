# -*- coding: utf-8 -*-
from golingo.settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': "::memory::",
}

# LOGGING_CONFIG = True
