from selenium.webdriver.common.by import By
from tests import get_url
from webium.base_page import BasePage
from webium.controls.link import Link
from webium.find import Find


class AlertPage(BasePage):
    alert_link = Find(Link, By.ID, 'alert')
    '''@type: Link'''
    open_new_window_link = Find(Link, By.ID, 'open-new-window')
    '''@type : Link'''

    def __init__(self):
        super(AlertPage, self).__init__(url=get_url('alerts.html'))
