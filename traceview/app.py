# -*- coding: utf-8 -*-

"""
traceview.app

This module contains the objects associated with App Management API resources.

http://dev.appneta.com/docs/api-v2/app.html

"""

from .resource import Resource


class Assign(Resource):

    PATH = "assign_app"
