# -*- coding: utf-8 -*-

"""
TraceView API library

:copyright: (c) 2014 by Daniel Riti.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'traceview'
__version__ = '0.2.0'
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

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")

    """

    def __init__(self, api_key):
        self.api_key = api_key

        #: Get all :py:class:`Actions <traceview.discovery.Action>` that have
        #: been traced.
        self.actions = Action(self.api_key)

        #: Get all available :py:class:`Apps <traceview.discovery.App>`.
        self.apps = App(self.api_key)

        #: Get all :py:class:`Browsers <traceview.discovery.Browser>` used by
        #: end users.
        self.browsers = Browser(self.api_key)

        #: Get all :py:class:`Controllers <traceview.discovery.Controller>` that
        #: have been traced.
        self.controllers = Controller(self.api_key)

        #: Get all :py:class:`Domains <traceview.discovery.Domain>` that have
        #: been traced.
        self.domains = Domain(self.api_key)

        #: See :py:class:`Errors <traceview.errors.Rate>`.
        self.errors = Error(self.api_key)

        #: Get all :py:class:`Hosts <traceview.discovery.Host>` that have been
        #: traced.
        self.hosts = Host(self.api_key)

        #: Get server or client latency information. For more details, check out
        #: :py:class:`Series <traceview.latency.Series>`,
        #: :py:class:`Summary <traceview.latency.Summary>`, and
        #: :py:class:`ByLayer <traceview.latency.ByLayer>`.
        self.latency = Latency(self.api_key)

        #: Get all recent :py:class:`Layers <traceview.discovery.Layer>` for an
        #: application.
        self.layers = Layer(self.api_key)

        #: Get all available :py:class:`Host Metrics <traceview.discovery.Metric>`
        #: that have been collected.
        self.metrics = Metric(self.api_key)

        #: Get :py:class:`Organization <traceview.organization.Organization>`
        #: and :py:class:`User <traceview.organization.User>` information.
        self.organization = Organization(self.api_key)

        #: Get all geographical :py:class:`Regions <traceview.discovery.Region>`
        #: of end users.
        self.regions = Region(self.api_key)
