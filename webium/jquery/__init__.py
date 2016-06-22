from webium.driver import get_driver


class JQuery(object):
    """ JQuery class provides jQuery wrapper for Selenium WebElement.

    Example (set element's value attr through jQuery.val function):
      e = driver.find_element_by_id('id_name')
      JQuery(e).val('New name')
    """
    JQUERY_PATH = './webium/jquery/jquery-1.10.2.js'

    def __init__(self, element):
        self.driver = get_driver()
        if not self.driver.execute_script('return window.jQuery'):
            with open(self.JQUERY_PATH, 'r') as jquery:
                self.driver.execute_script(jquery.read())
        self.element = element

    def __getattr__(self, name):
        def jquery_func(*args):
            jquery = 'return $(arguments[0]).{func}({args});'.format(
                func=name,
                args=','.join(['arguments[%d]' % (1 + i) for i in range(len(args))])
            )
            return self.driver.execute_script(jquery, self.element, *args)
        return jquery_func
