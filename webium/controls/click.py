from selenium.webdriver.remote.webelement import WebElement

from webium.jquery import JQuery


class Clickable(WebElement):

    def click(self, jquery=False):
        """
        Click by WebElement, if not, JQuery click
        """
        if jquery:
            e = JQuery(self)
            e.click()
        else:
            super(Clickable, self).click()
