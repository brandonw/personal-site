Personal Site
==============================

My personal website.


LICENSE: BSD

Settings
------------

Personal Site relies extensively on environment settings which **will not work with Apache/mod_wsgi setups**. It has been deployed successfully with both Gunicorn/Nginx and even uWSGI/Nginx.

For configuration purposes, the following table maps the 'Personal Site' environment variables to their Django setting:

======================================= =========================== ============================================== ===========================================
Environment Variable                    Django Setting              Development Default                            Production Default
======================================= =========================== ============================================== ===========================================
DJANGO_DATABASES                        DATABASES                   See code                                       See code
DJANGO_DEBUG                            DEBUG                       True                                           False
DJANGO_EMAIL_BACKEND                    EMAIL_BACKEND               django.core.mail.backends.console.EmailBackend django.core.mail.backends.smtp.EmailBackend
DJANGO_SECRET_KEY                       SECRET_KEY                  CHANGEME!!!                                    raises error
======================================= =========================== ============================================== ===========================================

Getting up and running
----------------------

1. Run ``vagrant up`` to create, start, and provision your development virtual machine.
2. Run ``vagrant ssh`` to ssh into the newly provisioned virtual machine.
3. Run ``python /vagrant/personal-site/manage.py createsuperuser`` to create a superuser

You can now run ``grunt serve`` while SSHed into the ``/vagrant`` directory to serve the app, which you can then view from your host at localhost:8000. In addition, the uwsgi server will be reloaded automatically upon file changes.

Note that when any included dependency changes its static files, you must run ``collectstatic -l -i sass`` to update the staticfiles directory, which is where nginx forwards ``/static`` requests to.
