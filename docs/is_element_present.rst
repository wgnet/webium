is_element_present
==================

Typical task in test scripts is to check if an element is present.
Each container (BasePage, physical and logical) has ``is_element_present`` method.
It returns if an element with corresponding name is shown on the page.

.. literalinclude:: ../examples/12_is_element_present.py

*Note*: Containers with elements located via ``Finds`` also support
``is_element_present``, albeit with special behaviour. Since the attribute will
be a list of elements, rather than a single element, ``True`` will be returned
only if all elements in the list are present. In the event that no elements are
found (i.e. an empty list), or one or more elements do not qualify as present,
``False`` will be returned.

just_in_dom
-----------

By default ``is_element_present`` returns ``True`` only if an element is visible.
If you want to have ``True`` returned in cases when the element just present in DOM - set ``just_in_dom=True``

timeout
-------
``timeout`` in seconds allows you to wait for ``True`` value.

*Note:* if an element is not shown this option will delay ``False`` value from being returned.
