#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for TraceView API Library

"""

import unittest

from traceview.formatters import tuplify


class TestTuplifyTimeseries(unittest.TestCase):

    results = None

    def setUp(self):
        self.results = {
            'fields': ['one', 'two', 'three'],
            'items': [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        }

    def test_tuplify_length(self):
        actual = tuplify(self.results)
        self.assertEqual(len(actual), 3)

    def test_tuplify_properties(self):
        actual = tuplify(self.results)
        self.assertEqual(actual[0].one, 1)
        self.assertEqual(actual[1].two, 5)
        self.assertEqual(actual[2].three, 9)

    def test_tuplify_name(self):
        actual = tuplify(self.results, 'Lol')
        self.assertEqual(actual[0].__class__.__name__, 'LolTuple')


class TestTuplifyDict(unittest.TestCase):

    results = None

    def setUp(self):
        self.results = {
            'reqs_per_time_period': '0.27/sec',
            'total_requests': 980
        }

    def test_tuplify_length(self):
        actual = tuplify(self.results)
        self.assertEqual(actual.total_requests, 980)
        self.assertEqual(actual.reqs_per_time_period, '0.27/sec')
