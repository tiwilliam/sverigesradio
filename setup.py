# -*- coding: utf8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    version='0.3',
    name='sverigesradio',
    description='Python bindings for Sveriges Radio API',
    author='William Tisäter',
    author_email='william@defunct.cc',
    packages=['sverigesradio'],
    install_requires=['requests >= 2.1.0'],
    url='https://github.com/tiwilliam/sverigesradio',
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3'],
    license='MIT License',
    keywords='sr sverigesradio'
)
