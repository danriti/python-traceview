.. traceview documentation master file, created by
   sphinx-quickstart on Fri May  2 20:12:10 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-traceview
=====================================

Release v\ |version|.

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
    >>> tv = traceview.TraceView("API KEY HERE")
    >>> tv.apps()
    [u'Default', u'pyramid_web_app']
    >>> tv.latency.server.summary(app='Default')
    {u'count': 2746.0, u'average': 213911.87181354698, u'latest': 35209.87654320987}
    >>> tv.latency.client.summary(app='Default', time_window='week')
    {u'count': 70546.0, u'average': 10385458.60856746, u'latest': 138626.26463003372}
