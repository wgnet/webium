from selenium.webdriver import Firefox
from webium import BasePage


class DriverHandlingPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(DriverHandlingPage, self).__init__(url='http://wargaming.net/', *args, **kwargs)

if __name__ == '__main__':
    my_driver = Firefox()
    page = DriverHandlingPage(driver=my_driver)
    page.open()
    print('Page title: ' + my_driver.title)
    my_driver.quit()
