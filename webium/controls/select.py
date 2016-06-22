from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class Select(WebElement):
    """
    Implements logic to work with Web List UI elements
    """

    @property
    def is_multiple(self):
        value = self.get_attribute('multiple')
        return value is not None and not value == 'false'

    def select_option(self, option):
        """
        Performs selection of provided item from Web List

        @params option - string item name
        """
        items_list = self.get_options()
        for item in items_list:
            if item.get_attribute("value") == option:
                item.click()
                break

    def get_options(self):
        """
        Performs search for provided item in Web List
        """
        return self.find_elements_by_tag_name('option')

    def get_attribute_selected(self, attribute):
        """
        Performs search of selected item from Web List
        Return attribute of selected item

        @params attribute - string attribute name
        """
        items_list = self.get_options()
        return next(iter([item.get_attribute(attribute) for item in items_list if item.is_selected()]), None)

    def get_value_selected(self):
        """
        Performs search of selected item from Web List
        Return value of selected item
        """
        return self.get_attribute_selected('value')

    def get_text_selected(self):
        """
        Performs search of selected item from Web List
        Return text of selected item
        """
        return self.get_attribute_selected('text')

    def select_by_visible_text(self, text):
        """
        Performs search of selected item from Web List

        @params text - string visible text
        """
        xpath = './/option[normalize-space(.) = {0}]'.format(self._escape_string(text))
        opts = self.find_elements_by_xpath(xpath)
        matched = False
        for opt in opts:
            self._set_selected(opt)
            if not self.is_multiple:
                return
            matched = True
        # in case the target option isn't found by xpath
        # attempt to find it by direct comparison among options which contain at least the longest token from the text
        if len(opts) == 0 and ' ' in text:
            sub_string_without_space = self._get_longest_token(text)
            if sub_string_without_space == "":
                candidates = self.get_options()
            else:
                xpath = ".//option[contains(.,{0})]".format(self._escape_string(sub_string_without_space))
                candidates = self.find_elements_by_xpath(xpath)
            for candidate in candidates:
                if text == candidate.text:
                    self._set_selected(candidate)
                    if not self.is_multiple:
                        return
                    matched = True
        if not matched:
            raise NoSuchElementException("Could not locate element with visible text: " + str(text))

    @staticmethod
    def _escape_string(value):
        if '"' in value and "'" in value:
            substrings = value.split('"')
            result = ['concat(']
            for substring in substrings:
                result.append('"{0}"'.format(substring))
                result.append(', \'"\', ')
            result.pop()
            if value.endswith('"'):
                result.append(', \'"\'')
            return ''.join(result) + ')'

        if '"' in value:
            return "'{0}'".format(value)

        return '"{0}"'.format(value)

    @staticmethod
    def _get_longest_token(value):
        items = value.split(' ')
        longest = ''
        for item in items:
            if len(item) > len(longest):
                longest = item
        return longest

    @staticmethod
    def _set_selected(option):
        if not option.is_selected():
            option.click()
