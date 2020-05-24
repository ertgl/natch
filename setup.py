#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup


setup(
    name='natch',
    version='1.0.0',
    keywords='functional paradigm pattern matching',
    description='Pattern matching library.',
    license='MIT',
    author='Ertuğrul Keremoğlu',
    author_email='ertugkeremoglu@gmail.com',
    url='https://github.com/ertgl/natch/',
    classifiers=[
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    packages=[
        'natch',
        'natch.abstract',
        'natch.core',
        'natch.decorators',
        'natch.exceptions',
        'natch.hashers',
        'natch.rules',
    ],
    install_requires=[],
)
