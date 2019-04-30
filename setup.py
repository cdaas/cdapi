from setuptools import setup, find_packages

setup (
    name = 'cdapi',
    version='0.0.1',
    description='Container Desktop as a Service API',
    url='https://github.com/peak-oss/peakorc',
    author='CDaaS Development Team',
    author_email='post-issues@github.com',
    keywords='CDaaS api for OpenShift',
    packages=find_packages(),
    install_requires=['falcon','peewee','psycopg2-binary','requests','numpy',
                      'gunicorn', 'openshift']
)
