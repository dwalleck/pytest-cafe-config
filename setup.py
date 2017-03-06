#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-cafe-config',
    version='0.1.0',
    author='Daryl Walleck',
    author_email='dwalleck@gmail.com',
    maintainer='Daryl Walleck',
    maintainer_email='dwalleck@gmail.com',
    license='Apache Software License 2.0',
    url='https://github.com/dwalleck/pytest-cafe-config',
    description='Allows the use of the cafe configuration and logging with pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_cafe_config'],
    install_requires=['pytest>=2.9.2, opencafe'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'cafe-config = pytest_cafe_config',
        ],
    },
)
