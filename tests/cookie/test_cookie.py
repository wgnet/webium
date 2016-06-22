from http.cookiejar import Cookie
from unittest import TestCase

from nose.tools import eq_

from webium.cookie import convert_cookie_to_dict


class TestCookie(TestCase):

    def test_convert_cookie_to_dict(self):
        cook1 = {'name': 'cook1', 'value': 'value1', 'path': '/', 'secure': False, 'expiry': 1453912471}
        cookie = Cookie(
            0, cook1['name'], cook1['value'], None, False, '.github.com', True, True, cook1['path'], True,
            cook1['secure'], cook1['expiry'], False, None, None, None, False
        )
        dict1 = convert_cookie_to_dict(cookie)
        eq_(cook1, dict1)
