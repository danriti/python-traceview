.. traceview documentation master file, created by
   sphinx-quickstart on Fri May  2 20:12:10 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-traceview
================

Release v\ |version|.

Library for providing access to the TraceView API v2.

Please see the `TraceView API Reference <http://dev.appneta.com/docs/api-v2/reference.html>`_ for more information.

Installation
------------

To install python-traceview, simply:

.. code-block:: bash

    $ pip install python-traceview

Quick Start
-----------

Accessing information from TraceView is very simple.

Begin by importing the ``traceview`` module::

    >>> import traceview

Now, let's initialize a TraceView object using your TraceView access (API) key.
You can find this key on the **Organization Overview** page in TraceView::

    >>> tv = traceview.TraceView('API KEY HERE')

Now, we have a :py:class:`TraceView <traceview.TraceView>` object called ``tv``.
We can get all the information we need from this object.

For example, let's get all available applications setup within your TraceView
account::

    >>> tv.apps()
    [u'Default', u'pyramid_web_app']

Nice, right? We can also get a server side latency summary for the ``Default``
application::

    >>> tv.server.latency_summary(app='Default', time_window='hour')
    {u'count': 2746.0, u'average': 213911.87181354698, u'latest': 35209.87654320987}

TraceView has traced 2746 requests in the last hour, with an average latency of
213ms. That’s all well and good, but it’s also only the start of what information you
can get from TraceView.

API Documentation
-----------------

.. autoclass:: traceview.TraceView
   :members:

Latency
~~~~~~~

.. autoclass:: traceview.latency.Client
   :members:
.. autoclass:: traceview.latency.Server
   :members:
