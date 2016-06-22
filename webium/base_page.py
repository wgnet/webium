from types import MethodType
from waiting import TimeoutExpired
from selenium.common.exceptions import WebDriverException

import webium.settings
from webium.driver import get_driver
from webium.wait import wait
from webium.errors import WebiumException


def is_element_present(self, element_name, just_in_dom=False, timeout=0):
    def _get_driver():
        driver = getattr(self, '_driver', None)
        if driver:
            return driver
        return get_driver()

    _get_driver().implicitly_wait(timeout)
    try:
        def is_displayed():
            element = getattr(self, element_name, None)
            if not element:
                raise WebiumException('No element "{0}" within container {1}'.format(element_name, self))
            return element.is_displayed()

        is_displayed() if just_in_dom else wait(lambda: is_displayed(), timeout_seconds=timeout)
        return True
    except WebDriverException:
        return False
    except TimeoutExpired:
        return False
    finally:
        _get_driver().implicitly_wait(webium.settings.implicit_timeout)


class BasePage(object):
    url = None

    @property
    def _driver(self):
        if self.__driver:
            return self.__driver
        return get_driver()

    def __init__(self, driver=None, url=None):
        if url:
            self.url = url
        self.__driver = driver
        self.is_element_present = MethodType(is_element_present, self)

    def open(self):
        if not self.url:
            raise WebiumException('Can\'t open page without url')
        self._driver.get(self.url)

    def find_element(self, *args):
        return self._driver.find_element(*args)

    def find_elements(self, *args):
        return self._driver.find_elements(*args)

    def implicitly_wait(self, *args):
        return self._driver.implicitly_wait(*args)
