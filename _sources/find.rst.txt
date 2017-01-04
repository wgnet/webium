Find
====

``webium.find.Find`` finds a single element within page or other container.
By default found element class is ``WebElement``.

Main two parameters for Find are:

- ``by`` - what search strategy to use
- ``value`` - what value should be used to find an element

.. literalinclude:: ../examples/5_find.py

ui_type
-------
If you want to specify your own classes for controls ``ui_type`` is the parameter for ``Find`` to use your class.

.. literalinclude:: ../examples/6_find_ui_type.py

context
-------
There are cases when you can't specify page structure before actual run. Modern pages are dynamic and fuzzy.
If you can't specify Find as class attribute you should directly provide page object instance to perform search.

.. literalinclude:: ../examples/7_find_dynamic.py
