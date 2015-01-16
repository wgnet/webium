from selenium.webdriver.common.by import By
from tests.simple_page import SimplePageTest
from nose.tools import eq_, assert_raises
from webium.errors import WebiumException
from webium.find import Find


class WrongType(object):
    pass


class TestBase(SimplePageTest):
    def test_basic(self):
        eq_(self.page.one_line.text, 'A single line of text')

    def test_webelement_inheritance(self):
        assert_raises(WebiumException, Find, WrongType, By.ID, 'some_value')

    def test_default_search_type(self):
        eq_(self.page.default_search_type.text, 'A div containing\n'
                                                'More than one line of text\n'
                                                'and block level elements')

    def test_how_value_providing(self):
        assert_raises(WebiumException, Find, by=By.XPATH)
