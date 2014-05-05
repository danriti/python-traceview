# -*- coding: utf-8 -*-

"""
TraceView API library

:copyright: (c) 2014 by Daniel Riti.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'traceview'
__version__ = '0.3.0'
__author__ = 'Daniel Riti'
__license__ = 'MIT'


from .annotation import Annotation
from .app import Assign
from .discovery import Action, App, Browser, Controller, Domain, Host
from .discovery import Layer, Metric, Region
from .error import Rate
from .latency import Client, Server
from .organization import Organization, User


class TraceView(object):
    """ The :class:`TraceView <TraceView>` object.

    Provides access to TraceView API resources.

    :param api_key: The TraceView API access key.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView('API KEY HERE')

    """

    def __init__(self, api_key):
        self.api_key = api_key

        self._actions = Action(self.api_key)
        self._annotation = Annotation(self.api_key)
        self._apps = App(self.api_key)
        self._assign = Assign(self.api_key)
        self._browsers = Browser(self.api_key)
        self._controllers = Controller(self.api_key)
        self._domains = Domain(self.api_key)
        self._error_rates = Rate(self.api_key)
        self._hosts = Host(self.api_key)
        self._layers = Layer(self.api_key)
        self._metrics = Metric(self.api_key)
        self._organization = Organization(self.api_key)
        self._regions = Region(self.api_key)
        self._users = User(self.api_key)

        #: Get :py:class:`Client <traceview.latency.Client>` latency information.
        self.client = Client(self.api_key)
        #: Get :py:class:`Server <traceview.latency.Server>` latency information.
        self.server = Server(self.api_key)

    def actions(self):
        """ Get all actions that have been traced.

        :return: all actions traced.
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.actions()
          [u'admin', u'products', u'blog', u'settings', u'logout']

        """
        return self._actions.get()

    def annotation(self, message, *args, **kwargs):
        """ Create an annotation.

        Annotations are used to log arbitrary events into TraceView, which are
        used to understand the correlation between system events (i.e. code
        release, server restarts, etc) and performance trends.

        :param str message: The annotation message.
        :param str appname: (optional) The application to associate the annotation with.
        :param str hostname: (optional) The host to associate the annotation with.
        :param str username: (optional) The user name to associate the annotation with.
        :param str layer: (optional) The layer name to associate the annotation with.
        :param str time: (optional) The time to associate the annotation with, in seconds since the epoch.

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.annotation('Code deployed', appname='production_web')

        """
        kwargs['message'] = message
        self._annotation.post(*args, **kwargs)

    def apps(self):
        """ Get all available applications.

        :return: all available applications
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.apps()
          [u'Default', u'flask_app']

        """
        return self._apps.get()

    def assign(self, hostname, appname, *args, **kwargs):
        """ Assign a host to an existing application.

        Please note that you cannot join host names to the `Default`
        application, as all hosts start there.

        :param str hostname: The host name to assign to the application.
        :param str appname: The existing application name.
        :param str layer: (optional) The layer name to assign to the application.

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.assign(hostname='web-app-1234', appname='production_web')

        """
        kwargs['appname'] = appname
        kwargs['hostname'] = hostname
        self._assign.post(*args, **kwargs)

    def browsers(self):
        """ Get all browsers used by end users.

        :return: all browsers used by end users
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.browsers()
          [u'Chrome', u'Firefox', u'Links', u'Safari', u'Wii']

        """
        return self._browsers.get()

    def controllers(self):
        """ Get all controllers that have been traced.

        :return: all controllers traced
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.controllers()
          [u'admin', u'products', u'blog', u'settings', u'logout']

        """
        return self._controllers.get()

    def domains(self):
        """ Get all domains that have been traced.

        :return: all domains traced
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.domains()
          [u'example.com', u'www.example.com', u'mail.example.com']

        """
        return self._domains.get()

    def error_rates(self, app, *args, **kwargs):
        """ Get the error rate for an application.

        Each item in the items list is a pair of values (timestamp, error_rate).
        The error rate describes the number of traces with one or more errors,
        per total number of traces.

        :param str app: The application name.
        :return: timeseries data of the application's error rate
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.error_rates('Default')
          {u'fields': u'timestamp,error_rate', u'items': [[1399082880.0, 0], [1399082910.0, 0], ...]}

        """
        return self._error_rates.get(app, *args, **kwargs)

    def hosts(self):
        """ Get all hosts that have been traced.

        :return: all hosts traced
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.hosts()
          [u'db.example.com', u'api.example.com', u'www.example.com', u'mail.example.com']

        """
        return self._hosts.get()

    def layers(self, app, *args, **kwargs):
        """ Get all recent layers for an application.

        The default time window for reported layers is 1 day.

        :param str app: The app name to list layers.
        :param int since_time: (optional) The start of the time window as a UTC timestamp in milliseconds.
        :return: all available apps
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.layers('Default')
          [u'PHP', u'cURL', u'lighttpd', u'php_mysql', u'php_mysqli']

        """
        return self._layers.get(app, *args, **kwargs)

    def metrics(self):
        """ Get all available host metrics that have been collected.

        :return: all avaiable host metrics being collected.
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.metrics()
          [u'cpu_user_frac:all', u'load', u'mem_apps', u'mem_cached', u'mem_swap', u'mem_totalused', ... ]

        """
        return self._metrics.get()

    def organization(self):
        """ Get organization information.

        :return: organization information
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.organization()
          {u'fullname': u'the example organization', u'name': u'example'}

        """
        return self._organization.get()

    def regions(self):
        """ Get all geographical region codes of end users.

        Regions codes are ISO 3166-1 and ISO 3166-2 codes for all regions collected
        in RUM. Currently, country codes (ISO-3166-1) are available worldwide, and
        state codes (ISO-3166-2) are available in the US and Canada.

        :return: all geographical region codes of end users
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.regions()
          [u'CA', u'CA-BC', u'MX', u'RU', u'US', u'US-RI', ...]

        """
        return self._regions.get()

    def users(self):
        """ Get user information.

        :return: user information
        :rtype: list

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.organization.users()
          [{u'admin': True, u'name': u'Jane Doe', u'email': u'jdoe@example.com'}, { ... }]

        """
        return self._users.get()
