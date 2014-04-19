# -*- coding: utf-8 -*-

"""
traceview.discovery

This module contains the objects associated with Discovery API resources.

http://dev.appneta.com/docs/api-v2/discovery.html

"""

from .resource import Resource


class App(Resource):
    """ The :class:`App <App>` object.

    Returns a List of all available apps.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> apps = tv.apps()

    """

    PATH = "apps"


class Domain(Resource):
    """ The :class:`Domain <Domain>` object.

    Returns a List of all domains traced.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> domains = tv.domains()

    """

    PATH = "domains"


class Controller(Resource):
    """ The :class:`Controller <Controller>` object.

    Returns a List of all controllers traced.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> controllers = tv.controllers()

    """

    PATH = "controllers"


class Action(Resource):
    """ The :class:`Action <Action>` object.

    Returns a List of all actions traced.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> actions = tv.actions()

    """

    PATH = "actions"


class Browser(Resource):
    """ The :class:`Browser <Browser>` object.

    Returns a List of browser families, seen in RUM.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> browsers = tv.browsers()

    """

    PATH = "browsers"


class Host(Resource):
    """ The :class:`Host <Host>` object.

    Return a List of all hosts traced.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> hosts = tv.hosts()

    """

    PATH = "hosts"


class Metric(Resource):
    """ The :class:`Metric <Metric>` object.

    Return a List of all available host metrics being collected.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> metrics = tv.metrics()

    """

    PATH = "metrics"


class Region(Resource):
    """ The :class:`Region <Region>` object.

    Returns a list of region codes, seen in RUM.

    Regions codes are ISO 3166-1 and ISO 3166-2 codes for all regions collected
    in RUM. Currently, country codes (ISO-3166-1) are available worldwide, and
    state codes (ISO-3166-2) are available in the US and Canada.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> regions = tv.regions()

    """

    PATH = "regions"


class Layer(Resource):
    """ The :class:`Layer <Layer>` object.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> layers = tv.layers("Default")

    """

    PATH = "layers/{app}"

    def __call__(self, app, *args, **kwargs):
        """ Returns a List of all layers reporting data recently for the given
        app. The default time window for reported layers is 1 day.

        :param app: The app name to list layers.
        :param since_time: (optional) The start of the time window as a UTC timestamp in milliseconds.

        """
        self.path = self.PATH.format(app=app)
        return super(Layer, self).__call__(*args, **kwargs)
