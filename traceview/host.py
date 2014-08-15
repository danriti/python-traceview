# -*- coding: utf-8 -*-

"""
traceview.hosts

This module contains the objects associated with Hosts API resources.

http://dev.appneta.com/docs/api-v2/hosts.html

"""

from .resource import Resource


class Hosts(Resource):

    PATH = "hosts"

class Versions(Resource):

    PATH = "hosts/{host_id}/versions"

    def get(self, host_id, *args, **kwargs):
        """ Overloaded get method.

        :param str host_id: The host_id to list version information.

        """
        self.path = self.PATH.format(host_id=host_id)
        return super(Versions, self).get(*args, **kwargs)

class DeleteHost(Resource):

    PATH = "hosts/{host_id}"

    def delete(self, host_id, *args, **kwargs):
        """ Overloaded delete method.

        :param str host_id: The host_id to delete.

        """
        self.path = self.PATH.format(host_id=host_id)
        return super(DeleteHost, self).delete(*args, **kwargs)
