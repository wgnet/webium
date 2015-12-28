from unittest import TestCase
from webium.jquery import JQuery

from tests.simple_page import SimplePage
from nose.tools import eq_


class SimpleJQueryPage(SimplePage):
    def get_text_by_jquery(self):
        return JQuery(self.one_line).text()


class TestJQuery(TestCase):
    def test_jquery_call(self):
        page = SimpleJQueryPage()
        page.open()
        eq_(page.get_text_by_jquery(), 'A single line of text')
