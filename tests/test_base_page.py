from unittest import TestCase
from nose.tools import assert_raises
from webium.base_page import BasePage
from webium.errors import WebiumException


class PageWithoutUrl(BasePage):
    pass


class TestNoUrlValidation(TestCase):
    def test_no_url_validation(self):
        page = PageWithoutUrl()
        assert_raises(WebiumException, page.open)