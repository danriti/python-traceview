# -*- coding: utf-8 -*-

"""
traceview.formatters

This module contains functions used to format TraceView API results.

"""

from collections import namedtuple


def identity(results):
    return results


def tuplify(results, class_name='Result'):
    if 'fields' in results and 'items' in results:
        return _tuplify_timeseries(results, class_name)
    return _tuplify_dict(results, class_name)


def _tuplify_timeseries(results, class_name):
    tuple_name = '{name}Tuple'.format(name=class_name)
    nt = namedtuple(tuple_name, results['fields'])
    return map(nt._make, results['items'])


def _tuplify_dict(results, class_name):
    tuple_name = '{name}Tuple'.format(name=class_name)
    nt = namedtuple(tuple_name, results.keys())
    return nt(**results)
