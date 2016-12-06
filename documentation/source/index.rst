.. edl documentation master file, created by
   sphinx-quickstart on Sat Aug 08 22:38:29 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to edl's documentation!
===============================

A python module to handle CMX 3600-like EDLs (Edit Decision Lists).

It uses a custom written grammar and antlr4 to do the actual parsing.

It can handle drop-frame timecodes, handles FROM CLIP comments and understands MOTION events (i.e. speed ups/downs).

Currently it does not handle dissolves.

Released under `LGPL <https://www.gnu.org/licenses/lgpl-3.0-standalone.html>`_

Contents:

.. toctree::
   :maxdepth: 2

   edl.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
