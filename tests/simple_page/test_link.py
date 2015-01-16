from tests.simple_page import SimplePageTest
from tests import get_url
from nose.tools import eq_


class TestClick(SimplePageTest):
    def test_link(self):
        eq_(self.page.icon_link.get_href(), get_url('icon.gif'))