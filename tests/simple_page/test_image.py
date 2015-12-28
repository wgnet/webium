from nose.tools import ok_, eq_

from tests import get_url
from tests.simple_page import SimplePageTest


class ImageClick(SimplePageTest):
    def test_image_is_displayed(self):
        self.page.valid_image.click()
        ok_(self.page.valid_image.is_displayed())
        ok_(not self.page.image_with_bad_src.is_displayed())

    def test_get_src(self):
        eq_(self.page.valid_image.get_src(), get_url("icon.gif"))
