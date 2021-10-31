Supported web servers
---------------------

This extension can be used to create Flask routes that handle WebSocket
requests when used with `Werkzeug <https://werkzeug.palletsprojects.com/>`_,
`Gunicorn <https://gunicorn.org/>`_, `Eventlet <https://eventlet.net/>`_ or
`Gevent <http://www.gevent.org/>`_. The following sections describe deployment
details specific to each of these web servers.

Werkzeug (Flask development web server)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Werkzeug supports WebSocket routing in version 2, which means that this 
extension can only be used with versions of Flask starting at 2.0.

To run your application use the normal method that you always use. Both the 
``flask run`` and ``app.run()`` methods of starting the Flask application
should work.

Gunicorn
~~~~~~~~

To use this package with Gunicorn you need to keep in mind that each active
WebSocket client will use up a worker. For that reason, the most practical way
to run a WebSocket server is to use the ``--threads`` option to allocate the
number of clients that you need::

    gunicorn -b :5000 --threads 100 module:app

It is also okay to use multiple workers, each with a number of allocated
threads::

    gunicorn -b :5000 --workers 4 --threads 100 module:app

Eventlet
~~~~~~~~

To serve your application with the eventlet WSGI server you can use the
following script::

    import eventlet
    eventlet.monkey_patch()

    from eventlet import wsgi
    from module import app

    wsgi.server(eventlet.listen(('', 5000)), app)

It is also possible to use Gunicorn's eventlet worker::

    gunicorn -b :5000 --worker-class eventlet module:app

Gunicorn's eventlet worker handles a maximum of 1000 concurrent requests in a
single worker process by default. The maximum number of concurrent requests can
be changed with the ``--worker-connections`` option. The number of workers can
be changed with the ``--workers`` option.

Gevent
~~~~~~

To serve your application with the gevent WSGI server you can use the
following script::

    from gevent import monkey
    monkey.patch_all()

    from gevent.pywsgi import WSGIServer
    from module import app

    WSGIServer(('127.0.0.1', 5000), app).serve_forever()

It is also possible to use Gunicorn's gevent worker::

    gunicorn -b :5000 --worker-class gevent module:app

Gunicorn's gevent worker handles a maximum of 1000 concurrent requests in a
single worker process by default. The maximum number of concurrent requests can
be changed with the ``--worker-connections`` option. The number of workers can
be changed with the ``--workers`` option.

Unlike other WebSocket packages for Gevent, this extension does not require the
``gevent-websocket`` package to be installed.
