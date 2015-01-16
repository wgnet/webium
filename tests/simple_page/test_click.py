from webium.driver import get_driver
from tests.simple_page import SimplePageTest
from nose.tools import ok_, assert_false


class TestClick(SimplePageTest):
    def test_basic_click(self):
        self.page.icon_link.click()
        ok_(get_driver().current_url.endswith('icon.gif'), 'Page after click wasn\'t opened')

    def test_jquery_click(self):
        assert_false(self.page.checkbox.is_selected())
        self.page.checkbox.click(True)
        ok_(self.page.checkbox.is_selected())
