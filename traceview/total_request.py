# -*- coding: utf-8 -*-

"""
traceview.total_request

This module contains the objects associated with Total Requests API resources.

http://dev.appneta.com/docs/api-v2/total_requests.html

"""

from .resource import Resource


class TotalRequests(Resource):

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
