from selenium.webdriver.common.by import By
from webium import BasePage, Find


class SomePage(BasePage):
    join_link = Find(by=By.CSS_SELECTOR, value='a[href*="registration"]')

    def __init__(self):
        super(SomePage, self).__init__(url='http://wargaming.net')


if __name__ == '__main__':
    page = SomePage()
    page.open()
    page.join_link.click()
