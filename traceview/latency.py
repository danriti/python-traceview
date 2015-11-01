# -*- coding: utf-8 -*-

"""
traceview.latency

This module contains the objects associated with Latency API resources.

http://dev.appneta.com/docs/api-v2/latency.html

"""

from .resource import Resource


class Server(Resource):
    """ The :class:`Server <Server>` class.

    Get server side latency information.

    """

    def latency_series(self, app, *args, **kwargs):
        """ Get a timeseries line of the applications latency and volume.

        Each timeseries point is a triple of (timestamp, volume, latency).

        :param str app: The app name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :param str domain: (optional) The domain to filter on.
        :param str url: (optional) The url path to filter on.
        :param str layer: (optional) The application layer to filter on.
        :param str controller: (optional) The controller to filter on.
        :param str action: (optional) The action to filter on.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.server.latency_series('Default')
          {u'fields': u'timestamp,volume,avg_latency', u'items': [[1399089120.0, 27.0, 226074.07407407407], ...]}

        """
        path = 'latency/{app}/server/series'.format(app=app)
        return self.api.get(path, *args, **kwargs)

    def latency_summary(self, app, *args, **kwargs):
        """ Get a summary of the latency and volume traced.

        :param str app: The app name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :param str domain: (optional) The domain to filter on.
        :param str url: (optional) The url path to filter on.
        :param str layer: (optional) The application layer to filter on.
        :param str controller: (optional) The controller to filter on.
        :param str action: (optional) The action to filter on.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.server.latency_summary('Default')
          {u'count': 2402.0, u'average': 271437.13572023314, u'latest': 19530.61224489796}

        """
        path = 'latency/{app}/server/summary'.format(app=app)
        return self.api.get(path, *args, **kwargs)

    def latency_by_layer(self, app, *args, **kwargs):
        """ Get timeseries data grouped by application layers.

        :param str app: The app name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :param str domain: (optional) The domain to filter on.
        :param str url: (optional) The url path to filter on.
        :param str layer: (optional) The application layer to filter on.
        :param str controller: (optional) The controller to filter on.
        :param str action: (optional) The action to filter on.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        Usage::

          >>> import pprint
          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.server.latency_by_layer('Default')
          >>> pprint.pprint(tv.server.latency_by_layer('Default'))
          [{u'layer': u'PHP',
            u'timeseries': {u'fields': u'timestamp,volume,avg_latency',
                            u'items': [[1399089540.0, 10, 0], ...]}},
           ...
          ]

        """
        path = 'latency/{app}/server/by-layer'.format(app=app)
        return self.api.get(path, *args, **kwargs)


class Client(Resource):
    """ The :class:`Client <Client>` class.

    Get client side latency information.

    """

    def latency_series(self, app, *args, **kwargs):
        """ Get a timeseries line of the applications latency and volume.

        Each timeseries point is a triple of (timestamp, volume, latency).

        :param str app: The app name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :param str domain: (optional) The domain to filter on.
        :param str url: (optional) The url path to filter on.
        :param str layer: (optional) The application layer to filter on.
        :param str controller: (optional) The controller to filter on.
        :param str action: (optional) The action to filter on.
        :param str browser: (optional) The browser to filter on.
        :param str region: (optional) The region to filter on.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.client.latency_series('Default')
          {u'fields': u'timestamp,volume,avg_latency', u'items': [[1399090230.0, 0, None], ...]}

        """
        path = 'latency/{app}/client/series'.format(app=app)
        return self.api.get(path, *args, **kwargs)

    def latency_summary(self, app, *args, **kwargs):
        """ Get a summary of the latency and volume traced.

        :param str app: The app name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :param str domain: (optional) The domain to filter on.
        :param str url: (optional) The url path to filter on.
        :param str layer: (optional) The application layer to filter on.
        :param str controller: (optional) The controller to filter on.
        :param str action: (optional) The action to filter on.
        :param str browser: (optional) The browser to filter on.
        :param str region: (optional) The region to filter on.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.client.latency_summary('Default')
          {u'count': 93.0, u'average': 14503082.720430108, u'latest': None}


        """
        path = 'latency/{app}/client/summary'.format(app=app)
        return self.api.get(path, *args, **kwargs)
