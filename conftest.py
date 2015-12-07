import os
from django.conf import settings


def pytest_configure():
    if not settings.configured:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'golingo.settings_test'
        os.environ['LOGGING_CONFIG'] = None
