from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement
from webium.driver import get_driver

__author__ = 'a_bul'


class Image(WebElement):
    def get_src(self):
        return self.get_attribute('src')

    def is_displayed(self):
        is_node_displayed = super(Image, self).is_displayed()
        script = 'return (typeof arguments[0].naturalWidth!="undefined" && arguments[0].naturalWidth>0);'
        is_image_loaded = lambda: self._execute(Command.EXECUTE_SCRIPT, {'script': script, 'args': [self]})['value']
        return is_node_displayed and is_image_loaded()
