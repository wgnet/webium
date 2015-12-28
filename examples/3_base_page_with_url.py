from webium import BasePage


class PageWithUrl(BasePage):
    def __init__(self):
        super(PageWithUrl, self).__init__(url='http://wargaming.com/')

if __name__ == '__main__':
    page = PageWithUrl()
    page.open()
