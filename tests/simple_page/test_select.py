from nose.tools import ok_, eq_

from tests.simple_page import SimplePageTest


class TestSelect(SimplePageTest):
    def test_is_multiple(self):
        ok_(self.page.multi_select.is_multiple)
        ok_(not self.page.simple_select.is_multiple)

    def test_select_option(self):
        self.page.simple_select.select_option('2')
        eq_(self.page.simple_select.get_value_selected(), '2')

    def test_select_by_text(self):
        self.page.simple_select.select_by_visible_text('black')
        eq_(self.page.simple_select.get_text_selected(), 'black')

    def test_get_options(self):
        eq_(len(self.page.simple_select.get_options()), 3)
        eq_(len(self.page.multi_select.get_options()), 3)

    def test_get_value_selected(self):
        self.page.simple_select.select_by_visible_text('red')
        eq_(self.page.simple_select.get_value_selected(), '1')
        eq_(self.page.multi_select.get_value_selected(), '2')

    def test_get_text_selected(self):
        self.page.simple_select.select_option('1')
        eq_(self.page.simple_select.get_text_selected(), 'red')
        eq_(self.page.multi_select.get_text_selected(), 'green')
