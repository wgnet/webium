from nose.tools import assert_raises, ok_
from selenium.common.exceptions import NoSuchElementException
from tests.simple_page import SimplePageTest
import webium.driver
from webium.no_implicitly_wait import no_wait
import webium.settings
import time


class TestNoWaitDecorator(SimplePageTest):
    def test_no_wait_decorator(self):
        webium.driver.get_driver().implicitly_wait(30)
        start = time.time()
        self.method_with_decorator()
        exec_time = time.time() - start
        ok_(exec_time < 3, 'Execution took too much time: ' + str(exec_time))

    def tearDown(self):
        webium.driver.get_driver().implicitly_wait(webium.settings.implicit_timeout)

    @no_wait
    def method_with_decorator(self):
        assert_raises(NoSuchElementException, getattr, self.page, 'unexistent_element')
