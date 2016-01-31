import sys

from distutils.core import setup

__author__ = 'noescobar'

setup(
    name='channels_test',
    version='0.1',
    description='',
    author='noescobar',
    author_email='nelson.holic@gmail.com',
    url='',
    install_requires=[
        "django<=1.10",
        'autobahn',
        "channels",
        "djangorestframework<=3.4",
        "celery",
        'django-celery>=3.1.16',
        "psycopg2"
    ]
)
