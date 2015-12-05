# -*- coding: utf-8 -*-
import os
# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'golingo.settings'


def before_all(context):
    import wsgi_intercept
    from django.core.handlers.wsgi import WSGIHandler
    host = context.host = 'localhost'
    port = context.port = 8000
    wsgi_intercept.add_wsgi_intercept(host, port, WSGIHandler)

    def browser_url(url):
        """Create a URL for the virtual WSGI server.

        e.g context.browser_url('/'), context.browser_url(reverse('my_view'))
        """
        return 'http://' + host + ':' + str(port) + url

    context.browser_url = browser_url


def before_scenario(context, scenario):
    import mechanicalsoup
    context.browser = mechanicalsoup.Browser()
