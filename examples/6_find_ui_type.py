from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find


class Link(WebElement):
    def is_secure(self):
        return self.get_attribute('href').startswith('https://')


class TypedPage(BasePage):
    join_link = Find(Link, By.CSS_SELECTOR, 'a[href*="registration"]')

    def __init__(self):
        super(TypedPage, self).__init__(url='http://wargaming.net')


if __name__ == '__main__':
    page = TypedPage()
    page.open()
    print('Is link secure: ' + str(page.join_link.is_secure()))
