# -*- coding: utf-8 -*-

"""
traceview.total_request

This module contains the objects associated with Total Requests API resources.

http://dev.appneta.com/docs/api-v2/total_requests.html

"""

from .resource import Resource


class TotalRequests(Resource):

    def __call__(self, *args, **kwargs):
        """ In previous versions of this library, there used to be a
        `total_requests` method on the `TraceView` object. Thus, this is
        implemented to maintain backwards compatibility.

        All new callers should use the methods defined.

        """
        return self.series(*args, **kwargs)

    def series(self, app, *args, **kwargs):
        """ Get a timeseries of the applications total requests.

        :param app: The application name.

        """
        path = 'total_requests/{app}/series'.format(app=app)
        return self.api.get(path, *args, **kwargs)

    def summary(self, app, *args, **kwargs):
        """ Get a summary of the applications total requests.

        :param app: The application name.

        """
        path = 'total_requests/{app}/summary'.format(app=app)
        return self.api.get(path, *args, **kwargs)
