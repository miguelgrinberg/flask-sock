"""
Flask-Sock
----------

WebSocket support for Flask.
"""
from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='flask-sock',
    version='0.0.2',
    url='http://github.com/miguelgrinberg/flask-sock/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguel.grinberg@gmail.com',
    description='WebSocket support for Flask.',
    long_description=long_description,
    py_modules=['flask_sock'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'flask',
        'werkzeug>=2.0.0rc3',
        'wsproto',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
