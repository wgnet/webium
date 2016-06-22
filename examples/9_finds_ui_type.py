from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Finds


class Link(WebElement):
    def is_secure(self):
        return self.get_attribute('href').startswith('https://')


class TypedPage(BasePage):
    links = Finds(Link, By.TAG_NAME, 'a')

    def __init__(self):
        super(TypedPage, self).__init__(url='http://wargaming.net')

    def get_unsecured_links(self):
        return filter(lambda link: not link.is_secure(), self.links)


if __name__ == '__main__':
    page = TypedPage()
    page.open()
    print('Number of unsecured links: ' + str(len(page.get_unsecured_links())))
