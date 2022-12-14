Challenge stack
===============

|CircleCI|

This application is a sample REST API provided for the eduNEXT developer
challenge.

The application you develop should interact with this app as it would do
with other applications on our production environment. There is no need
to modify the code running here.

Rationale
=========

This part of the challenge tests your ability to initialize a similar
stack to the ones we use during everyday development. Also in the real
world you are not always in control of the complete infrastructure and
stack. You need to make your own solutions work as pieces of the puzzle.

Getting started
===============

To get you started on the challenge quickly, we have created some
bootstrapping scripts to make things easier.

In plain language all you need to do is create a virtualenv[^1] and run
the bootstrap target with make.

A detailed step by step description is:

::

   cd 001_challenge_stack
   virtualenv venv
   source venv/bin/activate
   make bootstrap
   make run

The development server should have started now. You can visit the API by
navigating in a browser to :
``http://localhost:8010/api/v1/customerdata/``.

Imagine that what you just launched is the service where we keep
information of all our customers. Each customer gets an unique ID. For
example ``1b2f7b83-7b4d-441d-a210-afaa970e5b76``, then you can interact
with the data for any specific customer using the URL
``http://localhost:8010/api/v1/customerdata/1b2f7b83-7b4d-441d-a210-afaa970e5b76``.
You can find the IDs for all the customers and the object for each
customer by looking at the development server in a browser.

Now leave this running and move to the step 002 of the challenge. If you
mess up your work later, you can come back and use ``make erase`` to
clear everything again. Then start over at the step 2 of the list.

--------------

A guide on how to install virtualenv for Linux, Mac and Windows is
available here (no need to do the django part):
http://pythoncentral.io/how-to-install-python-django-windows-mac-linux/

Disclaimer: this instructions were tested using a linux OS, if you have
problems running this in a different OS, please let us know.

.. |CircleCI| image:: https://circleci.com/bb/macagua/edunext-challenge.svg?style=svg
   :target: https://circleci.com/bb/macagua/edunext-challenge
