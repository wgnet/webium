from time import time
from nose.tools import eq_, ok_
from selenium.webdriver import Firefox
from tests.simple_page import SimplePage


class TestCustomDriver(object):
    def setUp(self):
        self.driver = Firefox()
        self.driver.implicitly_wait(1)
        self.page = SimplePage(self.driver)
        self.page.open()

    def test_finds(self):
        start = time()
        eq_(len(self.page.empty_element_list), 0, 'List is not empty')
        ok_(time() - start < 1, 'Implicitly wait works in Finds')

    def test_nested_finds_in_container(self):
        start = time()
        eq_(len(self.page.physical_container.empty_element_list), 0, 'List is not empty')
        ok_(time() - start < 1, 'Implicitly wait works in Finds')

    def test_nested_finds_in_logical_container(self):
        start = time()
        eq_(len(self.page.logical_container.empty_element_list), 0, 'List is not empty')
        ok_(time() - start < 1, 'Implicitly wait works in Finds')

    def tearDown(self):
        self.driver.quit()
