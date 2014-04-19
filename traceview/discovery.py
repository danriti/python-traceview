# -*- coding: utf-8 -*-

"""
traceview.discovery

This module contains the objects associated with Discovery API resources.

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
    """ The :class:`Domains <Domains>` object.

    Returns a List of all domains traced.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> apps = tv.domains()

    """

    PATH = "domains"


class Layer(Resource):
    """ The :class:`Layer <Layer>` object.

    Returns a List of all layers reporting data recently for the given app.
    The default time window for reported layers is 1 day.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> layers = tv.layers("Default")

    """

    PATH = "layers/{app}"

    def __call__(self, app, *args, **kwargs):
        """ TBD.

        :param app: The app name to list layers.
        :param since_time: (optional) The start of the time window as a UTC timestamp in milliseconds.

        """
        self.PATH = self.PATH.format(app=app)
        return super(Layer, self).__call__(*args, **kwargs)
