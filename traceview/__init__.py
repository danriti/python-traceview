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


from .organization import Organization
from .discovery import Action, App, Browser, Controller, Domain, Host
from .discovery import Layer, Metric, Region
from .errors import Error
from .latency import Latency


class TraceView(object):
    """ The :class:`TraceView <TraceView>` object.

    Provides access to TraceView API resources.

    :param api_key: The TraceView API access key.

    """

    def __init__(self, api_key):
        self.api_key = api_key

        self.actions = Action(self.api_key)
        self.apps = App(self.api_key)
        self.browsers = Browser(self.api_key)
        self.controllers = Controller(self.api_key)
        self.domains = Domain(self.api_key)
        self.errors = Error(self.api_key)
        self.hosts = Host(self.api_key)
        self.latency = Latency(self.api_key)
        self.layers = Layer(self.api_key)
        self.metrics = Metric(self.api_key)
        self.organization = Organization(self.api_key)
        self.regions = Region(self.api_key)
