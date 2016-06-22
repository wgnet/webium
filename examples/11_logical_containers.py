from selenium.webdriver.common.by import By
from webium import Find, BasePage


class Header(object):
    sign_in = Find(by=By.CSS_SELECTOR, value='a[href*="auth/oid/new"]')
    register = Find(by=By.CSS_SELECTOR, value='a[href*="registration"]')


class StructuredPage(BasePage):
    # here we are just grouping Header elements together without any influence on actual search
    header = Find(Header)

    def __init__(self):
        super(StructuredPage, self).__init__(url='http://wargaming.net')


if __name__ == '__main__':
    page = StructuredPage()
    page.open()
    print(page.header.sign_in.text)
    print(page.header.register.text)
