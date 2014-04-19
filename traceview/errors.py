# -*- coding: utf-8 -*-

"""
traceview.errors

This module contains the objects associated with Errors API resources.

http://dev.appneta.com/docs/api-v2/errors.html

"""

from .resource import Resource


class Error(object):
    """ Object used to structurally organize the object call chain for Errors.

    """

    def __init__(self, *args, **kwargs):
        self.rate = Rate(*args, **kwargs)


class Rate(Resource):
    """ A :class:`Rate <Rate>` object.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> errors = tv.errors.rate("Default")

    """

    PATH = "errors/{app}/rate"

    def __call__(self, app, *args, **kwargs):
        """ Call the :class:`Series <Series>` object.

        Returns a Dictionary containing timeseries data of the application’s
        error rate.

        Each item in the items list is a pair of values (timestamp, error_rate).
        The error rate describes the number of traces with one or more errors,
        per total number of traces.

        :param app: The app name.

        """
        self.path = self.PATH.format(app=app)
        return super(Rate, self).__call__(*args, **kwargs)
