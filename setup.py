#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the Python KISS Module.

Source:: https://github.com/theskorm/kiss-fix
"""

import os
import setuptools
import sys

__title__ = 'kissfix'
__version__ = '7.0.7'
__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2017 Greg Albrecht and Contributors'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='Python KISS Module.',
    author='Greg Albrecht - patches by Michael Wheeler',
    author_email='oss@undef.net',
    packages=['kissfix'],
    package_data={'': ['LICENSE']},
    package_dir={'kissfix': 'kiss'},
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xssfox/kiss-fix',
    zip_safe=False,
    setup_requires=[
        'coverage >= 4.4.1',
        'nose >= 1.3.7',
        'dummyserial >= 1.0.0',
        'aprs > 6.9',
        'mocket >= 1.8.2'
    ],
    install_requires=['pyserial >= 3.4'],
    classifiers=[
        'Topic :: Communications :: Ham Radio',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'Ham Radio', 'APRS', 'KISS'
    ]
)
