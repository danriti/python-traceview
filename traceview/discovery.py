# -*- coding: utf-8 -*-

"""
traceview.discovery

This module contains the objects associated with Discovery API resources.

http://dev.appneta.com/docs/api-v2/discovery.html

"""

from .resource import Resource


class Action(Resource):

    PATH = "actions"


class App(Resource):

    PATH = "apps"


class Browser(Resource):

    PATH = "browsers"


class Controller(Resource):

    PATH = "controllers"


class Domain(Resource):

    PATH = "domains"


class Host(Resource):

    PATH = "hosts"


class Layer(Resource):

    PATH = "layers/{app}"

    def get(self, app, *args, **kwargs):
        """ Overloaded get method.

        :param str app: The app name to list layers.
        :param int since_time: (optional) The start of the time window as a UTC timestamp in milliseconds.

        """
        self.path = self.PATH.format(app=app)
        return super(Layer, self).get(*args, **kwargs)


class Metric(Resource):

    PATH = "metrics"


class Region(Resource):

    PATH = "regions"
