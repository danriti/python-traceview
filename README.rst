python-traceview
================

.. image:: https://badge.fury.io/py/python-traceview.png
    :target: http://badge.fury.io/py/python-traceview
.. image:: https://travis-ci.org/danriti/python-traceview.png?branch=master
    :target: https://travis-ci.org/danriti/python-traceview

Library for providing access to the TraceView API v2.

Please see the `TraceView API Reference <http://dev.appneta.com/docs/api-v2/reference.html>`_ for more information.

Installation
------------

To install python-traceview, simply:

.. code-block:: bash

    $ pip install python-traceview

Usage
-----

.. code-block:: python

    >>> import traceview
    >>> tv = traceview.TraceView('API KEY HERE')
    >>> tv.apps()
    [u'Default', u'pyramid_web_app']
    >>> tv.server.latency_summary(app='Default')
    {u'count': 2746.0, u'average': 213911.87181354698, u'latest': 35209.87654320987}
    >>> tv.error_rates('Default')
    {u'fields': u'timestamp,error_rate', u'items': [[1399082880.0, 0], [1399082910.0, 0], ...]}

Documentation
-------------

Documentation available at http://python-traceview.readthedocs.org/.
