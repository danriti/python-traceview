# -*- coding: utf-8 -*-

"""
traceview.annotation

This module contains the objects associated with Annotation API resources.

http://dev.appneta.com/docs/api-v2/annotations.html

"""

from .resource import Resource


class Annotation(Resource):

    PATH_POST = "log_message"
    PATH_GET_ALL = "annotations"
    PATH_GET_BY_APP = "app/{app}/annotations"

    def get(self, app=None, *args, **kwargs):
        """ Get annotations.

        :param app: (optional) The app name.

        """
        if app:
            self.path = self.PATH_GET_BY_APP.format(app=app)
        else:
            self.path = self.PATH_GET_ALL
        return super(Annotation, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """ Post annotations.

        """
        self.path = self.PATH_POST
        return super(Annotation, self).post(*args, **kwargs)
