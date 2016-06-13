# -*- coding: utf-8 -*-

"""
traceview.formatters

This module contains functions used to format TraceView API results.

"""

from collections import namedtuple


def identity(results):
    return results


def tuplify(results, class_name='Result'):
    """ Format API results into `namedtuple`.

    Formats API results into `namedtuple`s. Supports tuplifying results that
    are either timeseries data or objects (dicts).

    :param results: TraceView API results.
    :param str class_name: (optional) Prefix string for naming of the namedtuple.

    Usage::

      >>> import traceview
      >>> from traceview.formatters import tuplify
      >>> tv = traceview.TraceView('API KEY HERE', tuplify)
      >>> tv.total_requests.summary('APP NAME HERE')
      ResultTuple(reqs_per_time_period=u'19.53/sec', total_requests=70293.0)

    """
    # is timeseries data
    if 'fields' in results and 'items' in results:
        return _tuplify_timeseries(results, class_name)
    # is an dict
    if hasattr(results, 'keys'):
        return _tuplify_dict(results, class_name)
    return results


def _tuplify_timeseries(results, class_name):
    tuple_name = '{name}Tuple'.format(name=class_name)
    nt = namedtuple(tuple_name, results['fields'])
    return [nt(*item) for item in results['items']]


def _tuplify_dict(results, class_name):
    tuple_name = '{name}Tuple'.format(name=class_name)
    nt = namedtuple(tuple_name, results.keys())
    return nt(**results)
