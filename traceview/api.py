# -*- coding: utf-8 -*-

"""
traceview.api

This module is responsible for communicating with the TraceView API.

"""

import logging

import requests


log = logging.getLogger(__name__)


class Api(object):
    """ The :class:`Api <Api>` object.

    Responsible for making HTTP requests to the TraceView API.

    """

    AUTHORITY = "https://api.tv.appneta.com"
    VERSION = "api-v2"
    __methods = [
        'get',
        'post',
        'delete'
    ]

    def __init__(self, api_key):
        self._api_key = api_key

    def get(self, path, *args, **kwargs):
        """ Perform a HTTP GET request.

        :param dict kwargs: (optional) Query parameters for the request.

        """
        return self._request(method='get', path=path, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        """ Perform a HTTP POST request.

        :param dict kwargs: (optional) Query parameters for the request.

        """
        return self._request(method='post', path=path, *args, **kwargs)

    def delete(self, path, *args, **kwargs):
        """ Perform a HTTP DELETE request.

        :param dict kwargs: (optional) Query paramters for the request.

        """
        return self._request(method='delete', path=path, *args, **kwargs)

    def _request(self, method, path, *args, **kwargs):
        """ Perform a HTTP request.

        :param str method: The HTTP method to perform on the request.
        :param str path: The HTTP path to request.
        :param dict kwargs: (optional) Query parameters for the request.

        """
        url = self._url(path)
        params = self._build_query_params(kwargs)

        method = method.lower()
        if method not in self.__methods:
            raise requests.HTTPError("HTTP method is unsupported: %s" % (method,))

        log.debug("%s %s %s" % (method.upper(), url, params,))

        request_method = getattr(requests, method)
        response = request_method(url, params=params, allow_redirects=False)
        if response.status_code != requests.codes.ok: # pylint: disable-msg=E1101
            raise requests.HTTPError(response.status_code, url, response.text)

        return response.json()['data']

    def _url(self, path):
        return "{0}/{1}/{2}".format(self.AUTHORITY, self.VERSION, path)

    def _build_query_params(self, params=None):
        """ Builds and returns a Dictionary of query parameters.

        :params: (optional) Dictionary of query parameters.

        """
        if not isinstance(params, dict):
            params = {}
        params.update({"key": self._api_key})
        return params
