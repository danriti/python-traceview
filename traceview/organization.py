# -*- coding: utf-8 -*-

"""
traceview.organization

This module contains the objects associated with Organization API resources.

http://dev.appneta.com/docs/api-v2/organization.html

"""

from .resource import Resource


class Organization(Resource):

    PATH = "organization"


class User(Resource):

    PATH = "organization/users"
