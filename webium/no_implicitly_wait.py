from functools import wraps

import webium.driver
import webium.settings


def no_wait(func):
    @wraps(func)
    def without_wait(*args, **kwargs):
        try:
            webium.driver.get_driver().implicitly_wait(0)
            return func(*args, **kwargs)
        finally:
            webium.driver.get_driver().implicitly_wait(webium.settings.implicit_timeout)

    return without_wait
