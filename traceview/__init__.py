# -*- coding: utf-8 -*-

"""
TraceView API library

:copyright: (c) 2014 by Daniel Riti.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'traceview'
__version__ = '0.1.0'
__author__ = 'Daniel Riti'
__license__ = 'MIT'


import resources


class TraceView(object):
    """ Provides access to TraceView API resources.

    :param api_key: The TraceView API access key.

    """

    def __init__(self, api_key):
        self.api_key = api_key

        self.organization = resources.Organization(self.api_key)
        self.apps = resources.App(self.api_key)
        self.layers = resources.Layer(self.api_key)
        self.latency = resources.Latency(self.api_key)
