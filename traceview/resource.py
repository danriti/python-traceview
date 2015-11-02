# -*- coding: utf-8 -*-

"""
traceview.resources

This module contains the objects associated with API resources.

"""


class Resource(object):
    """ The :class:`Resource <Resource>` object.

    Abstract class for TraceView API resources.

    """

    def __init__(self, api):
        self.api = api
