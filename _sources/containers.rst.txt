Containers
==========

When you are specifying your classes you can perform search within them.
Using this feature you can narrow search and handle dynamic pages without complex XPath.

In order to use within your custom objects just declare ``Find`` or ``Finds``
within your classes the same way as they are declared within page objects.

Consider the page with the following DOM structure:

.. image:: ./_static/containers.png

In order to perform search within each item in the list we can do the following:

.. literalinclude:: ../examples/10_containers.py