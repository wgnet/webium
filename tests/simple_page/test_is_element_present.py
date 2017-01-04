from tests.simple_page import SimplePageTest
from nose.tools import ok_, assert_false, assert_raises
from webium.errors import WebiumException


class TestIsElementPresent(SimplePageTest):
    def test_is_element_present(self):
        ok_(self.page.is_element_present('icon_link'))
        assert_false(self.page.is_element_present('unexistent_element'))

    def test_is_element_present_via_finds(self):
        ok_(self.page.is_element_present('anchor_list'))

    def test_is_element_present_via_finds_empty_list(self):
        assert_false(self.page.is_element_present('empty_element_list'))

    def test_no_attribute(self):
        assert_raises(WebiumException, self.page.is_element_present, 'no_such_attribute')
