# -*- coding: utf-8 -*-

"""
traceview.app

This module contains the objects associated with App Management API resources.

http://dev.appneta.com/docs/api-v2/app.html

"""

from .resource import Resource


class Assign(Resource):

    PATH = "assign_app"

class AppHosts(Resource):

    PATH = "app/{app}/hosts"

    def get(self, app, *args, **kwargs):
        """ Overloaded get method.

        :param str app: The app name to list hosts.

        """
        self.path = self.PATH.format(app=app)
        return super(AppHosts, self).get(*args, **kwargs)
