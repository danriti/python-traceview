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
    __methods = [
        'get',
        'post'
    ]

    def __init__(self, api_key):
        self.api_key = api_key
        self.path = self.PATH

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

    def request(self, method, *args, **kwargs):
        """ Perform a HTTP request.

        :params str method: The HTTP method to perform on the request.
        :param dict kwargs: (optional) Query parameters for the request.

        """
        params = self.build_query_params(kwargs)

        method = method.lower()
        if method not in self.__methods:
            raise requests.HTTPError("HTTP method is unsupported: %s" % (method,))

        if self.path is None:
            raise requests.URLRequired

        log.debug("%s %s %s" % (method.upper(), self.uri, params,))

        request_method = getattr(requests, method)
        response = request_method(self.uri, params=params, allow_redirects=False)
        if response.status_code != requests.codes.ok: # pylint: disable-msg=E1101
            raise requests.HTTPError(response.status_code, self.uri, response.text)

        return response.json()['data']

    def get(self, *args, **kwargs):
        """ Perform a HTTP GET request.

        :param dict kwargs: (optional) Query parameters for the request.

        """
        return self.request(method='get', *args, **kwargs)

    def post(self, *args, **kwargs):
        """ Perform a HTTP POST request.

        :param dict kwargs: (optional) Query parameters for the request.

        """
        return self.request(method='post', *args, **kwargs)
