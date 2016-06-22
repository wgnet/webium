from selenium.webdriver.common.by import By
from webium import BasePage, Find


class PresencePage(BasePage):
    join_link = Find(by=By.CSS_SELECTOR, value='a[href*="registration"]')
    no_such_link = Find(by=By.CSS_SELECTOR, value='a[href*="no_such_link"]')

    def __init__(self):
        super(PresencePage, self).__init__(url='http://wargaming.net')


if __name__ == '__main__':
    page = PresencePage()
    page.open()
    print('This should be True: ' + str(page.is_element_present('join_link')))
    print('This should be False: ' + str(page.is_element_present('no_such_link')))
