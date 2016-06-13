# -*- coding: utf-8 -*-

"""
traceview.total_request

This module contains the objects associated with Total Requests API resources.

http://dev.appneta.com/docs/api-v2/total_requests.html

"""

from .resource import Resource


class TotalRequests(Resource):

    def __call__(self, *args, **kwargs):
        """
        .. deprecated:: 0.7.0
            Use :func:`series <traceview.total_requests.TotalRequests.series>` instead.

        Get the total requests for an application.

        Each item in the items list is a pair of values (timestamp,
        total_requests).  total_requests is the number of requests to
        your application during that time period.

        :param str app: The application name.
        :return: timeseries data of the application's total requests
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.total_requests('APP NAME HERE')
          {u'fields': u'timestamp,total_requests', u'items': [[1444650840.0, 583.0], [1444650870.0, 591.0], ...]}

        """
        # In previous versions of this library, there used to be a
        # `total_requests` method on the `TraceView` object. Thus, this is
        # implemented to maintain backwards compatibility.
        return self.series(*args, **kwargs)

    def series(self, app, *args, **kwargs):
        """ Get the total requests for an application.

        Each item in the items list is a pair of values (timestamp,
        total_requests).  total_requests is the number of requests to
        your application during that time period.

        :param str app: The application name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :return: timeseries data of the application's total requests
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.total_requests.series('APP NAME HERE')
          {u'fields': u'timestamp,total_requests', u'items': [[1444650840.0, 583.0], [1444650870.0, 591.0], ...]}

        """
        path = 'total_requests/{app}/series'.format(app=app)
        return self.api.get(path, *args, **kwargs)

    def summary(self, app, *args, **kwargs):
        """ Get a summary of the applications total requests.

        :param app: The application name.
        :param str time_window: (optional) The time window ('hour', 'day', or 'week') to filter on.
        :param str time_end: (optional) The end time for the time window.
        :return: summary of the application's total requests
        :rtype: dict

        Usage::

          >>> import traceview
          >>> tv = traceview.TraceView('API KEY HERE')
          >>> tv.total_requests.summary('APP NAME HERE')
          {u'reqs_per_time_period': u'19.61/sec', u'total_requests': 70579.0}

        """
        path = 'total_requests/{app}/summary'.format(app=app)
        return self.api.get(path, *args, **kwargs)
