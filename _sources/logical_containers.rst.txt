Logical Containers
==================
Logical containers are classes that represent some part of user interface but there is no need to search for them.
Only child elements are found but they are found uniquely without nested searches (e.g. by id).

For example some menu should be placed on some of your pages but menu items have ids and you don't need
to narrow search by ordinary container.
In such case search will be performed globally on the page but elements are stored within Menu class.

The difference between logical and ordinary containers:

- inheritance from ``WebElement``, logical containers are not inherited from it
- when declaring a logical container in a Page Object class arguments for ``by`` and ``value`` parameters are not passed in ``Find`` call

.. literalinclude:: ../examples/11_logical_containers.py
