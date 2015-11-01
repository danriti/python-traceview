# -*- coding: utf-8 -*-

"""
traceview.hosts

This module contains the objects associated with Hosts API resources.

http://dev.appneta.com/docs/api-v2/hosts.html

"""

from .resource import Resource


class Host(Resource):

    def get(self, app=None):
        if app:
            path = 'app/{app}/hosts'.format(app=app)
        else:
            path = 'hosts'
        return self.api.get(path)

    def delete(self, host_id):
        path = 'hosts/{host_id}'.format(host_id=host_id)
        return self.api.delete(path)


class Instrumentation(Resource):

    def get(self, host_id):
        path = 'hosts/{host_id}/versions'.format(host_id=host_id)
        return self.api.get(path)
