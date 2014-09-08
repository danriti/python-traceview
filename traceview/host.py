# -*- coding: utf-8 -*-

"""
traceview.hosts

This module contains the objects associated with Hosts API resources.

http://dev.appneta.com/docs/api-v2/hosts.html

"""

from .resource import Resource


class Host(Resource):

    PATH = {
        "GET": "hosts",
        "GET_BY_APP": "app/{app}/hosts",
        "DELETE": "hosts/{host_id}"
    }

    def get(self, app=None, *args, **kwargs):
        """ Get hosts.

        :param str app: (optional) The application name.

        """
        if app:
            self.path = self.PATH["GET_BY_APP"].format(app=app)
        else:
            self.path = self.PATH["GET"]
        return super(Host, self).get(*args, **kwargs)

    def delete(self, host_id, *args, **kwargs):
        """ Delete host.

        :param str host_id: The host_id to delete.

        """
        self.path = self.PATH["DELETE"].format(host_id=host_id)
        return super(Host, self).delete(*args, **kwargs)


class Instrumentation(Resource):

    PATH = "hosts/{host_id}/versions"

    def get(self, host_id, *args, **kwargs):
        """ Get instrumentation versions for host.

        :param str host_id: The host_id to list version information.

        """
        self.path = self.PATH.format(host_id=host_id)
        return super(Instrumentation, self).get(*args, **kwargs)
