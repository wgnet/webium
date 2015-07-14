from types import MethodType
from selenium.webdriver.remote.webelement import WebElement
from webium.errors import WebiumException
from webium.base_page import is_element_present

import webium.settings


class Find(object):
    by = None
    value = None
    ui_type = None
    context = None
    _target_element = None
    init_args = None
    init_kwargs = None

    def __init__(self, ui_type=WebElement,
                 by=None,
                 value=None,
                 context=None,
                 *args,
                 **kwargs):
        self.by = by
        self.value = value
        if self.value and not self.by:
            self.by = webium.settings.default_search_type
        self.ui_type = ui_type
        self.context = context
        self._target_element = None
        self.init_args = args
        self.init_kwargs = kwargs
        self._validate_params()

    def _validate_params(self):
        if self.by and not self.value:
            raise WebiumException('Provide search value in addition to by')
        if not self.by:
            if issubclass(self.ui_type, WebElement):
                raise WebiumException('Logical containers shouldn\'t be WebElement')
        else:
            if not issubclass(self.ui_type, WebElement):
                raise WebiumException('UI types should inherit WebElement')

    def __get__(self, obj, *args):
        self.context = obj
        self._search_element()
        return self._target_element

    def __getattribute__(self, item):
        if hasattr(Find, item):
            return object.__getattribute__(self, item)
        self._search_element()
        return self._target_element.__getattribute__(item)

    def __getitem__(self, key):
        self._search_element()
        return self._target_element.__getitem__(key)

    def _search_element(self):
        if not self.context:
            raise WebiumException("Search context should be defined with dynamic Find usage." +
                                  " Please define context in __init__.")
        if (self.by is not None) and (self.value is not None):
            web_element = self.context.find_element(self.by, self.value)
            web_element.__class__ = self.ui_type
            self._target_element = web_element
        else:
            container = self.ui_type()
            container.find_element = self.context.find_element
            container.find_elements = self.context.find_elements
            self._target_element = container
        self._target_element.is_element_present = MethodType(is_element_present, self._target_element)
        self._target_element.implicitly_wait = self.context.implicitly_wait
        if len(self.init_args) or len(self.init_kwargs) > 0:
            self._target_element.__init__(*self.init_args, **self.init_kwargs)


class Finds(Find):
    def _validate_params(self):
        if not self.value:
            raise WebiumException('Provide value to search elements')
        if not issubclass(self.ui_type, WebElement):
            raise WebiumException('Finds is applicable only for WebElements')

    def _search_element(self):
        self.context.implicitly_wait(0)
        self._target_element = self.context.find_elements(self.by, self.value)
        self.context.implicitly_wait(webium.settings.implicit_timeout)
        for item in self._target_element:
            item.__class__ = self.ui_type
            item.is_element_present = MethodType(is_element_present, item)
            item.implicitly_wait = self.context.implicitly_wait
