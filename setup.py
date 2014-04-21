#!/usr/bin/env python

import traceview

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = []

requires = ['requests==2.2.1']

with open('README.md') as f:
    readme = f.read()

setup(
    name="python-traceview",
    version=traceview.__version__,
    description="TraceView API Client",
    long_description=readme,

    # The project URL.
    url='https://github.com/danriti/python-traceview',

    # Author details
    author='Daniel Riti',
    author_email='dmriti@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.1',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
    ],

    # What does your project relate to?
    keywords='traceview api client development performance',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages.
    packages=packages,

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed.
    install_requires=requires,

    package_dir={'traceview': 'traceview'},
)
