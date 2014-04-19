# -*- coding: utf-8 -*-

"""
traceview.resources

This module contains the objects associated with API resources.

"""

import logging

import requests


log = logging.getLogger(__name__)


class Resource(object):
    """ The Resource object.

    """

    AUTHORITY = "https://api.tv.appneta.com"
    VERSION = "api-v2"
    PATH = None

    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, *args, **kwargs):
        params = self.build_query_params(kwargs)
        return self.get(params=params)

    @property
    def path(self):
        return "{0}/{1}/{2}".format(self.AUTHORITY, self.VERSION, self.PATH)

    def build_query_params(self, params=None):
        """ Builds and returns a Dictionary of query parameters.

        :params: (optional) Dictionary of query parameters.

        """
        if not isinstance(params, dict):
            params = {}
        params.update({"key": self.api_key})
        return params

    def get(self, params=None):
        """ Perform a HTTP GET request for the given Resource.

        :params: (optional) Dictionary of query parameters.

        """
        if params is None:
            params = {}

        if self.path is None:
            raise Exception("Pump fake")

        log.debug(self.path, params)
        response = requests.get(self.path, params=params, allow_redirects=False)
        if response.status_code != requests.codes.ok: # pylint: disable-msg=E1101
            raise Exception(response.status_code, self.path, response.text)

        return response.json()['data']


class User(Resource):
    """ Returns a List of user data for your organization.

    """

    PATH = "organization/users"


class Organization(Resource):
    """ Returns a Dictionary of organization data.

    """

    PATH = "organization"

    def __init__(self, *args, **kwargs):
        super(Organization, self).__init__(*args, **kwargs)
        self.users = User(*args, **kwargs)


class App(Resource):
    """ Returns a List of all available apps.

    """

    PATH = "apps"


class Layer(Resource):
    """ Returns a List of all layers reporting data recently for the given app.
    The default time window for reported layers is 1 day.

    """

    PATH = "layers/{app}"

    def __call__(self, app, *args, **kwargs):
        """ TBD.

        :param app: The app name to list layers.
        :param since_time: (optional) The start of the time window as a UTC timestamp in milliseconds.

        """
        self.PATH = self.PATH.format(app=app)
        return super(Layer, self).__call__(*args, **kwargs)


class Latency(object):

    def __init__(self, *args, **kwargs):
        self.server = Server(*args, **kwargs)
        self.client = Client(*args, **kwargs)


class Server(object):

    def __init__(self, *args, **kwargs):
        self.series = Series("server", *args, **kwargs)
        self.summary = Summary("server", *args, **kwargs)
        self.by_layer = ByLayer("server", *args, **kwargs)


class Client(object):

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
        self.PATH = self.PATH.format(app=app, data_type=self.data_type)
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
        self.PATH = self.PATH.format(app=app, data_type=self.data_type)
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
        self.PATH = self.PATH.format(app=app, data_type=self.data_type)
        return super(ByLayer, self).__call__(*args, **kwargs)
