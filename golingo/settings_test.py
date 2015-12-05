# -*- coding: utf-8 -*-
__author__ = 'jesuejunior'
from golingo.settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': "::memory::",
}