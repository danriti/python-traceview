# -*- coding: utf-8 -*-

"""
traceview.annotation

This module contains the objects associated with Annotation API resources.

http://dev.appneta.com/docs/api-v2/annotations.html

"""

from .resource import Resource


class Annotation(Resource):

    PATH = "log_message"

class Annotations(Resource):

    PATH_ALL = "annotations"
    PATH_BY_APP = "app/{app}/annotations"

    def get(self, app=None, *args, **kwargs):
        """ Get annotations.

        :param app: (optional) The app name.

        """
        if app:
            self.path = self.PATH_BY_APP.format(app=app)
        else:
            self.path = self.PATH_ALL
        return super(Annotations, self).get(*args, **kwargs)
