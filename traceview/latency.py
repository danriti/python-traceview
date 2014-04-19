# -*- coding: utf-8 -*-

"""
traceview.latency

This module contains the objects associated with Latency API resources.

http://dev.appneta.com/docs/api-v2/latency.html

"""

from .resource import Resource


class Latency(object):
    """ Object used to structurally organize the object call chain for Latency.

    """

    def __init__(self, *args, **kwargs):
        self.server = Server(*args, **kwargs)
        self.client = Client(*args, **kwargs)


class Server(object):
    """ Object used to structurally organize the object call chain for Server.

    """

    def __init__(self, *args, **kwargs):
        self.series = Series("server", *args, **kwargs)
        self.summary = Summary("server", *args, **kwargs)
        self.by_layer = ByLayer("server", *args, **kwargs)


class Client(object):
    """ Object used to structurally organize the object call chain for Server.

    """

    def __init__(self, *args, **kwargs):
        self.series = Series("client", *args, **kwargs)
        self.summary = Summary("client", *args, **kwargs)


class Series(Resource):
    """ A :class:`Series <Series>` object.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> server_series = tv.latency.server.series("Default")
      >>> client_series = tv.latency.client.series("Default")

    """

    PATH = "latency/{app}/{data_type}/series"

    def __init__(self, data_type, *args, **kwargs):
        """ Construct a :class:`Series <Series>` object.

        :param data_type: The type of latency data, can be "server" or "client".

        """
        super(Series, self).__init__(*args, **kwargs)
        self.data_type = data_type

    def __call__(self, app, *args, **kwargs):
        """ Call the :class:`Series <Series>` object.

        Return a Dictionary that contains timeseries data of the applications
        latency and volume, either from a client-side or server-side
        perspective. Each point is a triple of (timestamp, volume, latency)

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app, data_type=self.data_type)
        return super(Series, self).__call__(*args, **kwargs)


class Summary(Resource):
    """ A :class:`Summary <Summary>` object.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> server_summary = tv.latency.server.summary("Default")
      >>> client_summary = tv.latency.client.summary("Default")

    """

    PATH = "latency/{app}/{data_type}/summary"

    def __init__(self, data_type, *args, **kwargs):
        """ Construct a :class:`Summary <Summary>` object.

        :param data_type: The type of latency data, can be "server" or "client".

        """
        super(Summary, self).__init__(*args, **kwargs)
        self.data_type = data_type

    def __call__(self, app, *args, **kwargs):
        """ Call the :class:`Summary <Summary>` object.

        Returns a Dictionary containing the summary of the latency and volume
        traced, for either the client side or the server side.

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app, data_type=self.data_type)
        return super(Summary, self).__call__(*args, **kwargs)


class ByLayer(Resource):
    """ A :class:`ByLayer <ByLayer>` object.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> server_summary = tv.latency.server.by_layer("Default")
      >>> client_summary = tv.latency.client.by_layer("Default")

    """

    PATH = "latency/{app}/{data_type}/by-layer"

    def __init__(self, data_type, *args, **kwargs):
        """ Construct a :class:`ByLayer <ByLayer>` object.

        :param data_type: The type of latency data, can be "server" or "client".

        """
        super(ByLayer, self).__init__(*args, **kwargs)
        self.data_type = data_type

    def __call__(self, app, *args, **kwargs):
        """ Call the :class:`ByLayer <ByLayer>` object.

        Returns a Dictionary containing the summary of the latency and volume
        traced, for either the client side or the server side.

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app, data_type=self.data_type)
        return super(ByLayer, self).__call__(*args, **kwargs)
