.. Webium documentation master file, created by sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Webium's documentation!
==================================

Webium is a Page Object pattern implementation library for Python (http://martinfowler.com/bliki/PageObject.html).

It allows you to extend WebElement class to your custom controls like Link, Button and group them as pages.

Main classes are:

- webium.Find
- webium.Finds
- webium.BasePage

.. literalinclude:: ../examples/1_basic_google.py

Contents:

.. toctree::
   :maxdepth: 2

   base_page
   find
   finds
   containers
   logical_containers
   is_element_present
   wait
   settings