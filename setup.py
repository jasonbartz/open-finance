#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import openfinance

setup(name='open-finance',
        version=openfinance.__version__,
        description='An ongoing project to catalog, query and run analyses against the freely available financial APIs. ',
        author=openfinance.__author__,
        author_email=openfinance.__author_email__,
        url='https://github.com/jasonbartz/open-finance',
        packages=['openfinance',],
        install_requires=['requests',],
        license=openfinance.__license__,
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities'
        ],
)