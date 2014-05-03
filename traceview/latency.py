# -*- coding: utf-8 -*-

"""
traceview.latency

This module contains the objects associated with Latency API resources.

http://dev.appneta.com/docs/api-v2/latency.html

"""

from .resource import Resource


class Server(object):
    """ The :class:`Server <Server>` class.

    Get server side latency information.

    :param api_key: The TraceView API access key.

    """

    def __init__(self, *args, **kwargs):
        self._series = Series("server", *args, **kwargs)
        self._summary = Summary("server", *args, **kwargs)
        self._by_layer = ByLayer("server", *args, **kwargs)

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
        return self._series.get(app, *args, **kwargs)

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
        return self._summary.get(app, *args, **kwargs)

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
        return self._by_layer.get(app, *args, **kwargs)


class Client(object):
    """ The :class:`Client <Client>` class.

    Get client side latency information.

    :param api_key: The TraceView API access key.

    """


    def __init__(self, *args, **kwargs):
        self._series = Series("client", *args, **kwargs)
        self._summary = Summary("client", *args, **kwargs)

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
        return self._series.get(app, *args, **kwargs)

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
        return self._summary.get(app, *args, **kwargs)


class Series(Resource):

    PATH = "latency/{app}/{data_type}/series"

    def __init__(self, data_type, *args, **kwargs):
        """ Construct a :class:`Series <Series>` object.

        :param data_type: The type of latency data, can be "server" or "client".

        """
        super(Series, self).__init__(*args, **kwargs)
        self.data_type = data_type

    def get(self, app, *args, **kwargs):
        """ Call the :class:`Series <Series>` object.

        Return a Dictionary that contains timeseries data of the applications
        latency and volume, either from a client-side or server-side
        perspective. Each point is a triple of (timestamp, volume, latency)

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app, data_type=self.data_type)
        return super(Series, self).get(*args, **kwargs)


class Summary(Resource):

    PATH = "latency/{app}/{data_type}/summary"

    def __init__(self, data_type, *args, **kwargs):
        """ Construct a :class:`Summary <Summary>` object.

        :param data_type: The type of latency data, can be "server" or "client".

        """
        super(Summary, self).__init__(*args, **kwargs)
        self.data_type = data_type

    def get(self, app, *args, **kwargs):
        """ Call the :class:`Summary <Summary>` object.

        Returns a Dictionary containing the summary of the latency and volume
        traced, for either the client side or the server side.

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app, data_type=self.data_type)
        return super(Summary, self).get(*args, **kwargs)


class ByLayer(Resource):

    PATH = "latency/{app}/{data_type}/by-layer"

    def __init__(self, data_type, *args, **kwargs):
        """ Construct a :class:`ByLayer <ByLayer>` object.

        :param data_type: The type of latency data, can be "server" or "client".

        """
        super(ByLayer, self).__init__(*args, **kwargs)
        self.data_type = data_type

    def get(self, app, *args, **kwargs):
        """ Call the :class:`ByLayer <ByLayer>` object.

        Returns a Dictionary containing the summary of the latency and volume
        traced, for either the client side or the server side.

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app, data_type=self.data_type)
        return super(ByLayer, self).get(*args, **kwargs)
