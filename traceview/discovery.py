# -*- coding: utf-8 -*-

"""
traceview.discovery

This module contains the objects associated with Discovery API resources.

http://dev.appneta.com/docs/api-v2/discovery.html

"""

from .resource import Resource


class Action(Resource):

    def get(self):
        return self.api.get('actions')


class Browser(Resource):

    def get(self):
        return self.api.get('browsers')


class Controller(Resource):

    def get(self):
        return self.api.get('controllers')


class Domain(Resource):

    def get(self):
        return self.api.get('domains')


class Layer(Resource):

    def get(self, app, *args, **kwargs):
        path = 'layers/{app}'.format(app=app)
        return self.api.get(path, *args, **kwargs)


class Metric(Resource):

    def get(self):
        return self.api.get('metrics')


class Region(Resource):

    def get(self):
        return self.api.get('regions')
