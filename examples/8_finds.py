from selenium.webdriver.common.by import By
from webium import BasePage, Finds


class LinksPage(BasePage):
    links = Finds(by=By.TAG_NAME, value='a')

    def __init__(self):
        super(LinksPage, self).__init__(url='http://wargaming.net')


if __name__ == '__main__':
    page = LinksPage()
    page.open()
    print('Number of links: ' + str(len(page.links)))
