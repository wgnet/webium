from nose.tools import eq_, assert_raises
from tests.simple_page import SimplePageTest, Container
from webium.errors import WebiumException
from webium.find import Find


class TestLogicalContainer(SimplePageTest):
    def test_logical_container(self):
        eq_(self.page.logical_container.span.text, 'An inline element')

    def test_type_validation(self):
        assert_raises(WebiumException, Find, Container)
