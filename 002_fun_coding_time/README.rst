=======
PyPalPP
=======

.. image:: https://circleci.com/bb/macagua/edunext-challenge.svg?style=svg
    :target: https://circleci.com/bb/macagua/edunext-challenge

PyPalPP means PyPal Payment Processor. This application is a REST API 
provided for the eduNEXT Backend developer challenge.


Getting started
===============

To get you started on the challenge quickly, we have created some bootstrapping 
scripts to make things easier.

In plain language all you need to do is create a virtualenv [#]_ and run the 
bootstrap target with make.

A detailed step by step description is:

::

	$ cd 002_fun_coding_time
	$ virtualenv --python=python3 venv
	$ source venv/bin/activate
	$ make bootstrap


Executing run server
====================

To executing the Django run server, executing the following commands:

::

    $ make run

The development server should have started now. You can visit the API by navigating 
in a browser to : `http://localhost:8011/api/v1/MAIN-ENDPOINT/ <http://localhost:8011/api/v1/MAIN-ENDPOINT/>`_.


Testing
=======

To run your tests, executing the following commands:

::

    $ make test

To run the test suite against all support Python versions (2.7 and 3.5), executing the following commands:

::

    $ make test-all

----

.. rubric:: Footnotes

.. [#] Virtualenv is a python utility to make development simple. A guide
       on how to install virtualenv for Linux, Mac and Windows is available 
       here (no need to do the django part): http://pythoncentral.io/how-to-install-python-django-windows-mac-linux/

       **Disclaimer**: this instructions were tested using a linux OS, if you 
       have problems running this in a different OS, please let us know.
