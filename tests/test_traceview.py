#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for TraceView API Library

"""

import os
import unittest

import traceview
import traceview.request
import traceview.resources


TV_API_KEY = os.environ.get("TV_API_KEY", None)


class TestTraceView(unittest.TestCase):

    def test_title(self):
        self.assertEqual(traceview.__title__, 'traceview')

    def test_initialize(self):
        tv = traceview.TraceView(None)
        self.assertIsInstance(tv, traceview.TraceView)


@unittest.skipIf(TV_API_KEY is None, "No TraceView API Key found in environment.")
class TestTraceViewAPI(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_organization(self):
        org = self.tv.organization()
        self.assertNotEqual(org, None)
        self.assertTrue('name' in org)

    def test_users(self):
        users = self.tv.organization.users()
        self.assertNotEqual(users, None)
        self.assertIsInstance(users, list)
        self.assertTrue(len(users) > 0)

    def test_apps(self):
        apps = self.tv.apps()
        self.assertNotEqual(apps, None)
        self.assertIsInstance(apps, list)
        self.assertTrue(len(apps) > 0)


class TestResource(unittest.TestCase):

    def test_initialize(self):
        r = traceview.resources.Resource(None)
        self.assertIsInstance(r, traceview.resources.Resource)


if __name__ == '__main__':
    unittest.main()
