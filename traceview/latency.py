# -*- coding: utf-8 -*-

"""
traceview.latency

This module contains the objects associated with Latency API resources.

http://dev.appneta.com/docs/api-v2/latency.html

"""

from .resource import Resource


class Server(object):
    """ Object used to structurally organize the object call chain for Server.

    """

    def __init__(self, *args, **kwargs):
        self._series = Series("server", *args, **kwargs)
        self._summary = Summary("server", *args, **kwargs)
        self._by_layer = ByLayer("server", *args, **kwargs)

    def latency_series(self, app, *args, **kwargs):
        """ Get a timeseries line of the applications latency and volume.

        Each timeseries point is a triple of (timestamp, volume, latency).

        :param str app: The app name.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        """
        return self._series.get(app, *args, **kwargs)

    def latency_summary(self, app, *args, **kwargs):
        """ Get a summary of the latency and volume traced.

        :param str app: The app name.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        """
        return self._summary.get(app, *args, **kwargs)

    def latency_by_layer(self, app, *args, **kwargs):
        """ Get timeseries data grouped by application layers.

        :param str app: The app name.
        :return: timeseries data of the application latency and volume
        :rtype: dict

        """
        return self._by_layer.get(app, *args, **kwargs)


class Client(object):
    """ Object used to structurally organize the object call chain for Server.

    """

    def __init__(self, *args, **kwargs):
        self._series = Series("client", *args, **kwargs)
        self._summary = Summary("client", *args, **kwargs)

    def latency_series(self, app, *args, **kwargs):
        return self._series.get(app, *args, **kwargs)

    def latency_summary(self, app, *args, **kwargs):
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
