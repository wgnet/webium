is_element_present
==================

Typical task in test scripts is to check if an element is present.
Each container (BasePage, physical and logical) has ``is_element_present`` method.
It returns if an element with corresponding name is shown on the page.

.. literalinclude:: ../examples/12_is_element_present.py

just_in_dom
-----------

By default ``is_element_present`` returns ``True`` only if an element is visible.
If you want to have ``True`` returned in cases when the element just present in DOM - set ``just_in_dom=True``

timeout
-------
``timeout`` in seconds allows you to wait for ``True`` value.

*Note:* if an element is not shown this option will delay ``False`` value from being returned.