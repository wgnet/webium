from nose.tools import eq_

from tests import get_url
from tests.simple_page import SimplePageTest


class TestClick(SimplePageTest):
    def test_link(self):
        eq_(self.page.icon_link.get_href(), get_url('icon.gif'))
