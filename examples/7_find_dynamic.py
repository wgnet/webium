from selenium.webdriver.common.by import By
from webium import BasePage, Find


class DynamicPage(BasePage):
    def __init__(self):
        super(DynamicPage, self).__init__(url='http://wargaming.net')

    def get_link_by_href(self, href):
        return Find(by=By.CSS_SELECTOR, value='a[href*="{0}"]'.format(href), context=self)

if __name__ == '__main__':
    page = DynamicPage()
    page.open()
    page.get_link_by_href('registration').click()
