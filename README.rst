Feedback/ Notes App
============

A simple application designed to allow users to create notes based on a specific day. Other users can then leave comments on existing notes or create notes of their own.

Intended for use in a small businesses where a shared, daily summary of a business day could be a useful tool.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

Current State
--------------

* Allows creation of notes

* Allows commenting on existing notes

* Allows restrictions on access based on the privilages of a user's type

* Three user types have been implemented:
  * Registered User
  * Manager
  * Admin

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.
