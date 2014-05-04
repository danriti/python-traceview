# -*- coding: utf-8 -*-

"""
traceview.error

This module contains the objects associated with Errors API resources.

http://dev.appneta.com/docs/api-v2/errors.html

"""

from .resource import Resource


class Rate(Resource):

    PATH = "errors/{app}/rate"

    def get(self, app, *args, **kwargs):
        """ Overloaded get method.

        :param app: The application name.

        """
        self.path = self.PATH.format(app=app)
        return super(Rate, self).get(*args, **kwargs)
