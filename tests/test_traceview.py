#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import traceview

class TestTraceView(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_title(self):
        self.assertEqual(traceview.__title__, 'traceview')

if __name__ == '__main__':
    unittest.main()
