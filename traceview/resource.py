# -*- coding: utf-8 -*-

"""
traceview.resources

This module contains the objects associated with API resources.

"""

import logging

import requests


log = logging.getLogger(__name__)


class Resource(object):
    """ The :class:`Resource <Resource>` object.

    Acts as a base class for TraceView API resources.

    """

    AUTHORITY = "https://api.tv.appneta.com"
    VERSION = "api-v2"
    PATH = None

    def __init__(self, api_key):
        self.api_key = api_key
        self.path = self.PATH

    def __call__(self, *args, **kwargs):
        params = self.build_query_params(kwargs)
        return self.get(params=params)

    @property
    def uri(self):
        return "{0}/{1}/{2}".format(self.AUTHORITY, self.VERSION, self.path)

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

        log.debug(self.uri, params)
        response = requests.get(self.uri, params=params, allow_redirects=False)
        if response.status_code != requests.codes.ok: # pylint: disable-msg=E1101
            raise Exception(response.status_code, self.uri, response.text)

        return response.json()['data']
