python-traceview
================

Library for providing access to the TraceView API v2.

Please see the `TraceView API Reference <http://dev.appneta.com/docs/api-v2/reference.html>` for more information.

Installation
------------

To install python-traceview, simply:

.. code-block:: bash

    $ pip install python-traceview

## Usage

.. code-block:: python

    >>> import traceview
    >>> tv = traceview.TraceView("API KEY HERE")
    >>> tv.apps()
    [u'Default', u'pyramid_web_app']
