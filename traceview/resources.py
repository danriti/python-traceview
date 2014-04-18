# -*- coding: utf-8 -*-

"""
traceview.resources

This module contains the objects associated with API resources.

"""

import requests


class Resource(object):
    """ The Resource object.

    """

    AUTHORITY = "https://api.tv.appneta.com"
    VERSION = "api-v2"
    PATH = None

    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self):
        """

        """
        return self.get()

    @property
    def path(self):
        return "{0}/{1}/{2}".format(self.AUTHORITY, self.VERSION, self.PATH)

    @property
    def params(self):
        return {"key": self.api_key}

    def get(self):
        """

        """
        response = requests.get(self.path, params=self.params, allow_redirects=False)
        if response.status_code == requests.codes.ok: # pylint: disable-msg=E1101
            return response.json().get('data', None)
        else:
            return None


class User(Resource):

    PATH = "organization/users"


class Organization(Resource):

    PATH = "organization"

    def __init__(self, *args, **kwargs):
        super(Organization, self).__init__(*args, **kwargs)
        self.users = User(*args, **kwargs)


class App(Resource):

    PATH = "apps"
