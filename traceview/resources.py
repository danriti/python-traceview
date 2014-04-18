# -*- coding: utf-8 -*-

"""
traceview.resources

This module contains the objects associated with API resources.

"""

import requests


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

    :param app: The app name to list layers.
    :param since_time: (optional) The start of the time window as a UTC timestamp in milliseconds.

    """

    PATH = "layers/{app}"

    def __call__(self, app, *args, **kwargs):
        self.PATH = self.PATH.format(app=app)
        return super(Layer, self).__call__(*args, **kwargs)
