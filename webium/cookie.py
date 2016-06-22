WEB_DRIVER_COOKIE_KEYS_MAP = {
    'name': 'name',
    'value': 'value',
    'path': 'path',
    'secure': 'secure',
    'expires': 'expiry'
}


def _to_unicode_if_str(s):
    if isinstance(s, bytes):
        try:
            return s.decode('utf-8')
        except UnicodeDecodeError:
            return s.decode('latin-1')
    else:
        return s


def convert_cookie_to_dict(cookie, keys_map=WEB_DRIVER_COOKIE_KEYS_MAP):
    """
    Converts an instance of Cookie class from cookielib to a dict.
    The names of attributes can be changed according to keys_map:.
    For example, this method can be used to create a cookie which compatible with WebDriver format.

    :param cookie: Cookie instance received from requests/sessions using url2lib or requests libraries.
    :param keys_map: The dict to map cookie attributes for different schemas. By default WebDriver format is used.
    :return:
    """

    cookie_dict = dict()

    for k in keys_map.keys():
        key = _to_unicode_if_str(keys_map[k])
        value = _to_unicode_if_str(getattr(cookie, k))
        cookie_dict[key] = value

    return cookie_dict


def add_cookies_to_web_driver(driver, cookies):
    """
    Sets cookies in an existing WebDriver session.
    """
    for cookie in cookies:
        driver.add_cookie(convert_cookie_to_dict(cookie))
    return driver
