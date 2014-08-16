# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import personal-site
version = personal-site.__version__

setup(
    name='Personal Site',
    version=version,
    author='',
    author_email='brandon.waskiewicz@gmail.com',
    packages=[
        'personal-site',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['personal-site/manage.py'],
)