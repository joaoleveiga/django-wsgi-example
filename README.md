django-wsgi-example
===================

This is a very basic boilerplate-like repo for tests with [Django](http://djangoproject.com/), [mod_wsgi](https://modwsgi.readthedocs.org/en/master/) and [Apache Webserver](http://httpd.apache.org/) integration.

This project assumes that the user wants to test this setup with a PostgreSQL database with a database called ``table`` whose owner is a ``test`` user with password ``test``.

## Instructions

1. Load up the project in a virtual environment.

Example setup:

    $ cd /opt
    $ git clone
    $ cd django-wsgi-example/
    $ virtualenv env
    $ . env/bin/activate
    $ pip install -r requirements.txt
    $ cd myproj/
    $ python manage.py makemigrations
    $ python manage.py migrate


2. Edit the apache conf

Open a file for a virtual host

    vi /etc/httpd/conf.d/djwsgi-example.conf

and add the following:

    Listen 8008

    <VirtualHost *:8008>
        WSGIScriptAlias / /opt/django-wsgi-example/myproj/myproj/wsgi.py
        WSGIDaemonProcess djwsgi-example python-path=/opt/django-wsgi-example/myproj:/opt/django-wsgi-example/env/lib/python2.7/site-packages
        WSGIProcessGroup djwsgi-example

        Alias /static/ /opt/django-wsgi-example/myproj/web/static/

        <Directory /opt/django-wsgi-example/myproj/web/static/>
            # Require all granted
            Order deny,allow
            Allow from all
        </Directory>
        
        <Directory /opt/django-wsgi-example/myproj/myproj>
            <Files wsgi.py>
                # Require all granted
                Order deny,allow
                Allow from all
            </Files>
        </Directory>
    </VirtualHost>

Cross your fingers while restarting Apache.

## Probable Solution

SELinux seems to not like this setup. A probable solution for systems with CentOS 6 and Apache is to do this:

    semanage fcontext -a -t httpd_sys_script_exec_t FILE_PATH
    restorecon -v FILE_PATH

To files that might be raising _Permission Denied_ errors. Take special notice to database shared libraries (e.g. ``_psycopg2.so``)


----

### License

(c) 2015 João Veiga

See ``LICENSE`` for more.
