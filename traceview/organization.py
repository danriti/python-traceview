# -*- coding: utf-8 -*-

"""
traceview.organization

This module contains the objects associated with Organization API resources.

http://dev.appneta.com/docs/api-v2/organization.html

"""

from .resource import Resource


class Organization(Resource):

    def get(self):
        return self.api.get('organization')

    def users(self):
        return self.api.get('organization/users')

    def licenses(self):
        return self.api.get('organization/licenses')
