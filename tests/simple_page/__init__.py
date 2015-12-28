from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import tests
from webium.base_page import BasePage
from webium.controls.checkbox import Checkbox
from webium.controls.image import Image
from webium.controls.link import Link
from webium.controls.select import Select
from webium.find import Find, Finds


class Container(WebElement):
    second_element_with_id = Find(by=By.XPATH, value='.//*[2]')
    empty_element_list = Finds(by=By.XPATH, value='.//a[@no_such_attribute]')


class SpanContainer(object):
    span = Find(by=By.TAG_NAME, value='span')
    empty_element_list = Finds(by=By.XPATH, value='.//a[@no_such_attribute]')


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
    image_with_bad_src = Find(Image, By.ID, 'ImgTagWithBadSrc')
    '''@type: Image'''
    valid_image = Find(Image, By.ID, 'validImgTag')
    '''@type: Image'''
    multi_select = Find(Select, By.ID, 'id_multiple_select')
    '''@type: Select'''
    simple_select = Find(Select, By.ID, 'id_select')
    '''@type: Select'''

    def __init__(self, driver=None):
        super(SimplePage, self).__init__(driver=driver, url=tests.get_url('simple_page.html'))

    paragraphs = Finds(by=By.TAG_NAME, value='p')
    anchor_list = Finds(Link, By.TAG_NAME, 'a')
    div_list = Finds(DivWithLink, By.TAG_NAME, 'div')
    empty_element_list = Finds(by=By.XPATH, value='.//a[@no_such_attribute]')


class SimplePageTest(TestCase):
    page = SimplePage()

    def setUp(self):
        self.page.open()
