python-traceview
=========

TraceView API access via Python

http://dev.appneta.com/docs/api-v2/reference.html

## Installation

To install python-traceview, simply:

```bash
$ pip install python-traceview
```

## Usage

```python
>>> import traceview
>>> tv = traceview.TraceView("API KEY HERE")
>>> tv.apps()
[u'Default', u'pyramid_web_app']
```
