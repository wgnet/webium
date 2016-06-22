from nose.tools import eq_, assert_false, ok_
from selenium.webdriver.common.by import By
from tests import get_url
from tests.simple_page import SimplePageTest
from webium.find import Finds


class TestClick(SimplePageTest):
    def test_basic_finds(self):
        eq_(self.page.paragraphs[4].get_attribute('id'), 'nbspandspaces')

    def test_dynamic_find(self):
        paragraphs = Finds(by=By.TAG_NAME, value='p', context=self.page.physical_container)
        eq_(paragraphs[1].text, 'after pre')

    def test_custom_elements(self):
        hrefs = [a.get_href() for a in self.page.anchor_list if a.get_href()]
        eq_(hrefs[0], get_url('resultPage.html'))

    def test_is_element_present(self):
        divs = self.page.div_list
        ok_(divs[11].is_element_present('first_link'))
        assert_false(divs[3].is_element_present('first_link'))

    def test_inner_search(self):
        eq_(self.page.div_list[11].first_link.get_href(), get_url('resultPage.html'))
