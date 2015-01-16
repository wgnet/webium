from selenium.common.exceptions import WebDriverException
from waiting import wait as wait_lib

import webium.settings


def wait(*args, **kwargs):
    """
    Wrapping 'wait()' method of 'waiting' library with default parameter values.
    WebDriverException is ignored in the expected exceptions by default.
    """
    kwargs.setdefault('sleep_seconds', (1, None))
    kwargs.setdefault('expected_exceptions', WebDriverException)
    kwargs.setdefault('timeout_seconds', webium.settings.wait_timeout)

    return wait_lib(*args, **kwargs)
