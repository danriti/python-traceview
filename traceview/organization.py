# -*- coding: utf-8 -*-

"""
traceview.organization

This module contains the objects associated with Organization API resources.

http://dev.appneta.com/docs/api-v2/organization.html

"""

from .resource import Resource


class Organization(Resource):
    """ The :class:`Organization <Organization>` object.

    Returns a Dictionary of organization data.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> tv.organization()

    """

    PATH = "organization"

    def __init__(self, *args, **kwargs):
        super(Organization, self).__init__(*args, **kwargs)
        self.users = User(*args, **kwargs)


class User(Resource):
    """ The :class:`User <User>` object.

    Returns a List of user data for your organization.

    Usage::

      >>> import traceview
      >>> tv = traceview.TraceView("API KEY HERE")
      >>> tv.organization.users()

    """

    PATH = "organization/users"
