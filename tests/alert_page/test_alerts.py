from unittest import TestCase
from nose.tools import assert_false, ok_, eq_
from tests.alert_page import AlertPage
from webium.windows_handler import WindowsHandler


class TestAlert(TestCase):
    def test_alert_presence(self):
        page = AlertPage()
        page.open()
        handler = WindowsHandler()
        assert_false(handler.is_alert_present())
        page.alert_link.click()
        ok_(handler.is_alert_present())
        eq_(handler.get_alert_text(), 'cheese')
        handler.accept_alert()
        assert_false(handler.is_alert_present())
