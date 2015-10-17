# -*- coding: utf-8 -*-

"""
traceview.total_request

This module contains the objects associated with Total Requests API resources.

http://dev.appneta.com/docs/api-v2/total_requests.html

"""

from .resource import Resource


class Requests(Resource):

    PATH = "total_requests/{app}/series"

    def get(self, app, *args, **kwargs):
        """ Overloaded get method

        :param app: The application name.

        """
        self.path = self.PATH.format(app=app)
        return super(Requests, self).get(*args, **kwargs)
