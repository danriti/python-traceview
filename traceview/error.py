# -*- coding: utf-8 -*-

"""
traceview.error

This module contains the objects associated with Errors API resources.

http://dev.appneta.com/docs/api-v2/errors.html

"""

from .resource import Resource


class Rate(Resource):

    def get(self, app, *args, **kwargs):
        path = 'errors/{app}/rate'.format(app=app)
        return self.api.get(path)
