#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for TraceView API Library

"""

import datetime
import os
import unittest

import traceview
import traceview.resources


TV_API_KEY = os.environ.get("TV_API_KEY", None)


class TestTraceView(unittest.TestCase):

    def test_title(self):
        self.assertEqual(traceview.__title__, 'traceview')

    def test_initialize(self):
        tv = traceview.TraceView(None)
        self.assertIsInstance(tv, traceview.TraceView)


@unittest.skipIf(TV_API_KEY is None, "No TraceView API Key found in environment.")
class TestOrganization(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_organization(self):
        org = self.tv.organization()
        self.assertNotEqual(org, None)
        self.assertIsInstance(org, dict)
        self.assertTrue('name' in org)

    def test_users(self):
        users = self.tv.organization.users()
        self.assertNotEqual(users, None)
        self.assertIsInstance(users, list)
        self.assertTrue(len(users) > 0)


@unittest.skipIf(TV_API_KEY is None, "No TraceView API Key found in environment.")
class TestDiscovery(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_apps(self):
        apps = self.tv.apps()
        self.assertNotEqual(apps, None)
        self.assertIsInstance(apps, list)
        self.assertTrue(len(apps) > 0)

    def test_layers(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)
        layers = self.tv.layers(apps[0])
        self.assertNotEqual(layers, None)
        self.assertIsInstance(layers, list)
        self.assertTrue(len(layers) > 0)

    def test_layers_since_time(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        # get a unix timestamp
        epoch = datetime.datetime(1970, 1, 1)
        timestamp = (datetime.datetime.now() - epoch).total_seconds()

        layers = self.tv.layers(apps[0], since_time=timestamp)
        self.assertNotEqual(layers, None)
        self.assertIsInstance(layers, list)
        self.assertTrue(len(layers) > 0)

    def test_domains(self):
        domains = self.tv.domains()
        self.assertNotEqual(domains, None)
        self.assertIsInstance(domains, list)
        self.assertTrue(len(domains) > 0)

    def test_controllers(self):
        controllers = self.tv.controllers()
        self.assertNotEqual(controllers, None)
        self.assertIsInstance(controllers, list)
        self.assertTrue(len(controllers) > 0)

    def test_actions(self):
        actions = self.tv.actions()
        self.assertNotEqual(actions, None)
        self.assertIsInstance(actions, list)
        self.assertTrue(len(actions) > 0)

    def test_browsers(self):
        browsers = self.tv.browsers()
        self.assertNotEqual(browsers, None)
        self.assertIsInstance(browsers, list)
        self.assertTrue(len(browsers) > 0)

    def test_hosts(self):
        hosts = self.tv.hosts()
        self.assertNotEqual(hosts, None)
        self.assertIsInstance(hosts, list)
        self.assertTrue(len(hosts) > 0)


@unittest.skipIf(TV_API_KEY is None, "No TraceView API Key found in environment.")
class TestLatency(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_latency_server_series(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        server_latency = self.tv.latency.server.series(apps[0])
        self.assertNotEqual(server_latency, None)
        self.assertIsInstance(server_latency, dict)
        self.assertTrue('items' in server_latency)

    def test_latency_client_series(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        client_latency = self.tv.latency.client.series(apps[0])
        self.assertNotEqual(client_latency, None)
        self.assertIsInstance(client_latency, dict)
        self.assertTrue('items' in client_latency)

    def test_latency_server_summary(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        server_summary = self.tv.latency.server.summary(apps[0])
        self.assertNotEqual(server_summary, None)
        self.assertIsInstance(server_summary, dict)
        self.assertTrue('average' in server_summary)

    def test_latency_client_summary(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        client_summary = self.tv.latency.client.summary(apps[0])
        self.assertNotEqual(client_summary, None)
        self.assertIsInstance(client_summary, dict)
        self.assertTrue('average' in client_summary)

    def test_latency_server_by_layer(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        server_by_layer = self.tv.latency.server.by_layer(apps[0])
        self.assertNotEqual(server_by_layer, None)
        self.assertIsInstance(server_by_layer, list)
        self.assertTrue(len(server_by_layer) > 0)


class TestResource(unittest.TestCase):

    def test_initialize(self):
        r = traceview.resources.Resource(None)
        self.assertIsInstance(r, traceview.resources.Resource)

    def test_build_query_params(self):
        r = traceview.resources.Resource("ABC123")
        actual = r.build_query_params({"foo":"bar", "lol":5})
        expected = {
            "key": "ABC123",
            "foo": "bar",
            "lol": 5
        }
        self.assertEqual(actual, expected)

    def test_build_query_params_no_args(self):
        r = traceview.resources.Resource("ABC123")
        actual = r.build_query_params()
        expected = {
            "key": "ABC123"
        }
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
