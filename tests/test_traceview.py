#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for TraceView API Library

"""

import datetime
import os
import unittest

from httmock import all_requests, response, with_httmock
import requests

import traceview
import traceview.api


TV_API_KEY = os.environ.get('TV_API_KEY', None)

# The total_requests API requires a non-default app to measure
TV_APP_NAME = os.environ.get('TV_APP_NAME', None)


################################################################################
# API Tests
################################################################################

@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
class TestOrganization(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_organization(self):
        org = self.tv.organization()
        self.assertNotEqual(org, None)
        self.assertIsInstance(org, dict)
        self.assertTrue('name' in org)

    def test_users(self):
        users = self.tv.users()
        self.assertNotEqual(users, None)
        self.assertIsInstance(users, list)
        self.assertTrue(len(users) > 0)

    def test_licenses(self):
        licenses = self.tv.licenses()
        self.assertNotEqual(licenses, None)
        self.assertIsInstance(licenses, dict)
        self.assertTrue('hosts_used' in licenses)


@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
class TestDiscovery(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_apps(self):
        apps = self.tv.apps()
        self.assertNotEqual(apps, None)
        self.assertIsInstance(apps, list)
        self.assertTrue(len(apps) > 0)

    @unittest.skipIf(TV_APP_NAME is None, "TV_APP_NAME must define a valid (non-Default) app in order to test the layers API.")
    def test_layers(self):
        layers = self.tv.layers(TV_APP_NAME)
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

    def test_metrics(self):
        metrics = self.tv.metrics()
        self.assertNotEqual(metrics, None)
        self.assertIsInstance(metrics, list)
        self.assertTrue(len(metrics) > 0)

    def test_regions(self):
        regions = self.tv.regions()
        self.assertNotEqual(regions, None)
        self.assertIsInstance(regions, list)
        self.assertTrue(len(regions) > 0)


@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
class TestErrors(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_error_rates(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        error_rates = self.tv.error_rates(apps[0])
        self.assertNotEqual(error_rates, None)
        self.assertIsInstance(error_rates, dict)
        self.assertTrue('items' in error_rates)

@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
@unittest.skipIf(TV_APP_NAME is None, 'TV_APP_NAME must define a valid (non-Default) app in order to test the total_requests API.')
class TestTotalRequests(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_total_requests(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        total_requests = self.tv.total_requests(TV_APP_NAME)
        self.assertNotEqual(total_requests, None)
        self.assertIsInstance(total_requests, dict)
        self.assertIn('items', total_requests)

    def test_total_requests_series(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        total_requests = self.tv.total_requests.series(TV_APP_NAME)
        self.assertNotEqual(total_requests, None)
        self.assertIsInstance(total_requests, dict)
        self.assertIn('items', total_requests)

    def test_total_requests_summary(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        total_requests = self.tv.total_requests.series(TV_APP_NAME)
        self.assertNotEqual(total_requests, None)
        self.assertIsInstance(total_requests, dict)


@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
class TestLatency(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_latency_server_series(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        server_latency = self.tv.server.latency_series(apps[0])
        self.assertNotEqual(server_latency, None)
        self.assertIsInstance(server_latency, dict)
        self.assertTrue('items' in server_latency)

    def test_latency_client_series(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        client_latency = self.tv.client.latency_series(apps[0])
        self.assertNotEqual(client_latency, None)
        self.assertIsInstance(client_latency, dict)
        self.assertTrue('items' in client_latency)

    def test_latency_server_summary(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        server_summary = self.tv.server.latency_summary(apps[0])
        self.assertNotEqual(server_summary, None)
        self.assertIsInstance(server_summary, dict)
        self.assertTrue('average' in server_summary)

    def test_latency_client_summary(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        client_summary = self.tv.client.latency_summary(apps[0])
        self.assertNotEqual(client_summary, None)
        self.assertIsInstance(client_summary, dict)
        self.assertTrue('average' in client_summary)

    def test_latency_server_by_layer(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        server_by_layer = self.tv.server.latency_by_layer(apps[0])
        self.assertNotEqual(server_by_layer, None)
        self.assertIsInstance(server_by_layer, list)
        self.assertTrue(len(server_by_layer) > 0)


@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
class TestAnnotation(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_annotation(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        results = self.tv.annotation('test annotation', username='dan')
        self.assertEqual(results, None)

    def test_annotations(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        results = self.tv.annotations()
        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)
        self.assertTrue('message' in results[0])

    def test_annotations_by_app(self):
        apps = self.tv.apps()
        self.assertTrue(len(apps) > 0)

        results = self.tv.annotations(appname='Default')
        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)
        self.assertTrue('message' in results[0])


@unittest.skipIf(TV_API_KEY is None, 'No TraceView API Key found in environment.')
class TestHost(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)
        self.hosts = self.tv.hosts()

    def test_hosts(self):
        hosts = self.tv.hosts()
        self.assertNotEqual(hosts, None)
        self.assertIsInstance(hosts, list)
        self.assertTrue(len(hosts) > 0)

    def test_hosts_by_app(self):
        hosts = self.tv.hosts(appname='Default')
        self.assertNotEqual(hosts, None)
        self.assertIsInstance(hosts, list)
        self.assertTrue(len(hosts) > 0)

    def test_instrumentation(self):
        host_id = self.hosts[0]['id']
        versions = self.tv.instrumentation(host_id=host_id)
        self.assertNotEqual(versions, None)
        self.assertIsInstance(versions, list)
        self.assertIsInstance(versions[0], dict)


@unittest.skipIf(TV_API_KEY is None, "No TraceView API Key found in environment.")
class TestApp(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView(TV_API_KEY)

    def test_app_assign(self):
        apps = [app for app in self.tv.apps() if app != 'Default']
        self.assertTrue(len(apps) > 0)

        results = self.tv.assign(appname=apps[0], hostname='test.example.com')
        self.assertEqual(results, None)

    def test_app_delete(self):
        TEST_APP_NAME = 'TEST_APP_ABC123'

        apps = [app for app in self.tv.apps() if app == TEST_APP_NAME]
        self.assertTrue(len(apps) == 0) # ensure we don't have an app with this name

        results = self.tv.assign(appname=TEST_APP_NAME, hostname='test.example.com', create=True, layer="test")

        results = self.tv.delete_app(app_name=TEST_APP_NAME)
        self.assertEqual(results, True)

################################################################################
# HTTP Mocks
################################################################################

@all_requests
def traceview_api_mock(url, request):
    headers = {'content-type': 'application/json'}
    content = {
        'data': {'foo': 'bar'},
        'response': 'ok'
    }
    return response(200, content, headers, None, 5, request)

@all_requests
def traceview_api_mock_forbidden(url, request):
    headers = {'content-type': 'application/json'}
    content = {
        'data': {'foo': 'bar'},
        'response': 'ok'
    }
    return response(403, content, headers, None, 5, request)


################################################################################
# Unit Tests
################################################################################

class TestTraceView(unittest.TestCase):

    def test_title(self):
        self.assertEqual(traceview.__title__, 'traceview')

    def test_initialize(self):
        tv = traceview.TraceView(None)
        self.assertIsInstance(tv, traceview.TraceView)


class TestApi(unittest.TestCase):

    api = None

    def setUp(self):
        self.api = traceview.api.Api('ABC123')

    def test_build_query_params(self):
        actual = self.api._build_query_params({'foo':'bar', 'lol':5})
        expected = {
            'key': 'ABC123',
            'foo': 'bar',
            'lol': 5
        }
        self.assertEqual(actual, expected)

    def test_build_query_params_bad_args(self):
        actual = self.api._build_query_params([])
        self.assertNotEqual(actual, None)
        self.assertIsInstance(actual, dict)

    def test_build_query_params_no_args(self):
        actual = self.api._build_query_params()
        expected = {
            'key': 'ABC123'
        }
        self.assertEqual(actual, expected)

    def test_url(self):
        self.assertEqual(self.api._url('lol'),
                         'https://api.tv.appneta.com/api-v2/lol')

    @with_httmock(traceview_api_mock)
    def test_request_get(self):
        results = self.api.get('lol')
        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)

    @with_httmock(traceview_api_mock)
    def test_request_post(self):
        results = self.api.post('lol')
        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)

    @with_httmock(traceview_api_mock)
    def test_request_delete(self):
        results = self.api.delete('lol')
        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)

    @with_httmock(traceview_api_mock_forbidden)
    def test_request_forbidden(self):
        with self.assertRaises(requests.HTTPError):
            self.api.get('lol')


def after_request(results):
    return 2


class TestApiHooks(unittest.TestCase):

    api = None

    def setUp(self):
        self.api = traceview.api.Api('ABC123', after_request)

    @with_httmock(traceview_api_mock)
    def test_after_request_hook(self):
        results = self.api.get('lol')
        self.assertEquals(results, 2)


if __name__ == '__main__':
    unittest.main()
