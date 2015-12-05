# -*- coding: utf-8 -*-
import os
# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'golingo.settings'


def before_all(context):
    import wsgi_intercept
    from django.core.handlers.wsgi import WSGIHandler
    from urllib.parse import urljoin
    host = context.host = 'localhost'
    port = context.port = 8000
    # NOTE: Nothing is actually listening on this port. wsgi_intercept
    # monkeypatches the networking internals to use a fake socket when
    # connecting to this port.
    wsgi_intercept.add_wsgi_intercept(host, port, WSGIHandler)

    def browser_url(url):
        """Create a URL for the virtual WSGI server.

        e.g context.browser_url('/'), context.browser_url(reverse('my_view'))
        """
        return urljoin('http://%s:%d/' % (host, port), url)

    context.browser_url = browser_url

    ### BeautifulSoup is handy to have nearby. (Substitute lxml or html5lib as you see fit)
    from bs4 import BeautifulSoup
    def parse_soup():
        """Use BeautifulSoup to parse the current response and return the DOM tree.
        """
        r = context.browser.response()
        html = r.read()
        r.seek(0)
        return BeautifulSoup(html)

    context.parse_soup = parse_soup


def before_scenario(context, scenario):
    import mechanicalsoup
    context.browser = mechanicalsoup.Browser()
