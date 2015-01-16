from webium.controls.click import Clickable

__author__ = 'Roman Syrtsov (r_syrtsov@wargaming.net)'


class Link(Clickable):
    """
    Implements logic to work with UI elements of type Link
    """
    def get_href(self):
        return self.get_attribute('href')
