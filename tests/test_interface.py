#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for TraceView API Library public interface

"""

import unittest

import traceview


class TestTraceViewInterface(unittest.TestCase):

    def setUp(self):
        self.tv = traceview.TraceView('')

    def assertMethodExists(self, obj, func_name):
        self.assertTrue(hasattr(obj, func_name))
        self.assertTrue(hasattr(getattr(obj, func_name), '__call__'))

    def test_methods_interface(self):
        self.assertMethodExists(self.tv, 'actions')
        self.assertMethodExists(self.tv, 'annotation')
        self.assertMethodExists(self.tv, 'annotations')
        self.assertMethodExists(self.tv, 'apps')
        self.assertMethodExists(self.tv, 'assign')
        self.assertMethodExists(self.tv, 'browsers')
        self.assertMethodExists(self.tv, 'controllers')
        self.assertMethodExists(self.tv, 'delete')
        self.assertMethodExists(self.tv, 'delete_app')
        self.assertMethodExists(self.tv, 'delete_host')
        self.assertMethodExists(self.tv, 'domains')
        self.assertMethodExists(self.tv, 'error_rates')
        self.assertMethodExists(self.tv, 'hosts')
        self.assertMethodExists(self.tv, 'instrumentation')
        self.assertMethodExists(self.tv, 'layers')
        self.assertMethodExists(self.tv, 'licenses')
        self.assertMethodExists(self.tv, 'metrics')
        self.assertMethodExists(self.tv, 'organization')
        self.assertMethodExists(self.tv, 'regions')
        self.assertMethodExists(self.tv, 'total_requests')
        self.assertMethodExists(self.tv, 'users')

    def test_client_interface(self):
        self.assertTrue(hasattr(self.tv, 'client'))
        self.assertMethodExists(self.tv.client, 'latency_series')
        self.assertMethodExists(self.tv.client, 'latency_summary')

    def test_server_interface(self):
        self.assertTrue(hasattr(self.tv, 'server'))
        self.assertMethodExists(self.tv.server, 'latency_by_layer')
        self.assertMethodExists(self.tv.server, 'latency_series')
        self.assertMethodExists(self.tv.server, 'latency_summary')

    def test_total_requests_interface(self):
        self.assertTrue(hasattr(self.tv, 'total_requests'))
        self.assertMethodExists(self.tv.total_requests, 'series')
        self.assertMethodExists(self.tv.total_requests, 'summary')
