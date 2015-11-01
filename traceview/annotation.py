# -*- coding: utf-8 -*-

"""
traceview.annotation

This module contains the objects associated with Annotation API resources.

http://dev.appneta.com/docs/api-v2/annotations.html

"""

from .resource import Resource


class Annotation(Resource):

    def get(self, app=None, *args, **kwargs):
        if app:
            path = 'app/{app}/annotations'.format(app=app)
        else:
            path = 'annotations'
        return self.api.get(path, *args, **kwargs)

    def create(self, message, *args, **kwargs):
        kwargs['message'] = message
        return self.api.post('log_message', *args, **kwargs)
