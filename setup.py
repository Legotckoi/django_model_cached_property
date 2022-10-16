# -*- coding: utf-8 -*-

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_model_cached_property',
    version='0.0.2',
    license='MIT License',
    description='Django model cached property',
    long_description=README,
    url='https://github.com/Legotckoi/django_model_cached_property/',
    author='Evgenii Legotckoi',
    author_email='legotskoy@gmail.com',
    keywords='django model cached property',

    include_package_data=True,
    install_requires=[
        'Django',
        'redis',
        'django-redis'
    ],
    zip_safe=False,
    packages=['django_model_cached_property'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
