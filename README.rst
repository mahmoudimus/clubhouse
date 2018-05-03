clubhouse
=========

A python client for the `clubhouse.io <https://clubhouse.io/api/rest/v2>`_ API

.. image:: https://travis-ci.org/mahmoudimus/clubhouse.png?branch=master
   :target: https://travis-ci.org/mahmoudimus/clubhouse


Install
-------

To install the latest release from PyPI::

    pip install clubhouse

Or to install the latest development version from Git::

    pip install git+git://github.com/mahmoudimus/clubhouse.git

Or to install the latest from source::

    git clone https://github.com/mahmoudimus/clubhouse.git
    cd clubhouse
    pip install .

You can also make a developer install if you plan on modifying the
source frequently::

    pip install -e .


Generate Client
---------------

This will parse the `Resources <https://clubhouse.io/api/rest/v2/#Resources>`_ section from `Clubhouse's <https://clubhouse.io>` documentation and generate `marshmallow <https://marshmallow.readthedocs.io/en/latest/>`_ schemas that can be used for interacting with the API::

     curl -O clubhouse-api.html https://clubhouse.io/api/rest/v2/
     python clubhouse/parser.py clubhouse-api.html -o clubhouse/models.py


Usage
-----

TODO


License
-------

``clubhouse`` is MIT Licensed library.


Contribute
----------

- Check for open issues or open a fresh issue to start a discussion around a
  feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the master
  branch (or branch off of it).
- Write a test which shows that the bug was fixed or that the feature
  works as expected.
- Send a pull request and bug the maintainer until it gets merged and
  published.
- Make sure to add yourself to the author's file in ``setup.py`` and the
  ``Contributors`` section below :)


Contributors
------------

- `@mahmoudimus <https://github.com/mahmoudimus>`_
