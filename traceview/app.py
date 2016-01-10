# -*- coding: utf-8 -*-

"""
traceview.app

This module contains the objects associated with App Discovery
and App Management API resources.

http://dev.appneta.com/docs/api-v2/discovery.html
http://dev.appneta.com/docs/api-v2/app.html

"""

from .resource import Resource


class Assign(Resource):

    PATH = "assign_app"

class App(Resource):

    PATH = {
        "GET": "apps",
        "DELETE": "app/{app_name}"
    }
    def get(self, *args, **kwargs):
        self.path = self.PATH["GET"]
        return super(App, self).get(*args, **kwargs)

    def delete(self, app_name, *args, **kwargs):
        """ Delete an app.

        :param str app_name: The name of the app to delete.
        """
        self.path = self.PATH["DELETE"].format(app_name=app_name)
        return super(App, self).delete(*args, **kwargs)
