BasePage
========
Page is the main concept of Page Object pattern.
In order to create your pages you should inherit ``webium.base_page.BasePage``.

.. literalinclude:: ../examples/2_base_page.py

url
---

If your page has static url you can specify it in ``__init__``.
After that you can use ``open()`` method to open your page.

url can be also defined as static attribute of your class.

.. literalinclude:: ../examples/3_base_page_with_url.py

driver
------

Pages should have some ``WebDriver`` instance in order to manipulate browser.
By default Webium will create the instance of ``WebDriver`` class specified in ```webium.settings.driver_class``.
If you want to get the instance of the the driver you can call ``webium.driver.get_driver()`` method.

``driver`` parameter in ``BasePage`` gives you an ability to handle WebDriver instance by yourself.

.. literalinclude:: ../examples/4_base_page_driver_handling.py