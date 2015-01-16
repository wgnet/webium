from unittest import TestCase
from selenium.webdriver.remote.webelement import WebElement
from webium.base_page import BasePage

import tests
from webium.find import Find, Finds
from webium.controls.link import Link
from selenium.webdriver.common.by import By
from webium.controls.checkbox import Checkbox


class Container(WebElement):
    second_element_with_id = Find(by=By.XPATH, value='.//*[2]')


class SpanContainer(object):
    span = Find(by=By.TAG_NAME, value='span')


class DivWithLink(WebElement):
    first_link = Find(Link, By.TAG_NAME, 'a')
    '''@type: Link'''


class SimplePage(BasePage):
    one_line = Find(by=By.ID, value='oneline')
    '''@type: WrongType'''
    icon_link = Find(Link, By.ID, 'validAnchorTag')
    checkbox = Find(Checkbox, By.ID, 'checkbox1')
    unexistent_element = Find(by=By.ID, value='no_such_id')
    physical_container = Find(Container, By.ID, 'div-with-pre')
    '''@type: Container'''
    default_search_type = Find(value='multiline')
    logical_container = Find(SpanContainer)
    '''@type: SpanContainer'''

    def __init__(self):
        super(SimplePage, self).__init__(url=tests.get_url('simple_page.html'))

    paragraphs = Finds(by=By.TAG_NAME, value='p')
    anchor_list = Finds(Link, By.TAG_NAME, 'a')
    div_list = Finds(DivWithLink, By.TAG_NAME, 'div')


class SimplePageTest(TestCase):
    page = SimplePage()

    def setUp(self):
        self.page.open()