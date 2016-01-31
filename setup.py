import sys

from distutils.core import setup

__author__ = 'noescobar'

setup(
    name='EonLt_web',
    version='1.6',
    description='',
    author='noescobar',
    author_email='nelson.holic@gmail.com',
    url='',
    install_requires=[
        "django<=1.10",
        "channels",
        "djangorestframework<=3.4",
        "celery",
        'django-celery>=3.1.16',
        "psycopg2"
    ]
)
