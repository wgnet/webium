# Webium

[![PyPI](https://img.shields.io/pypi/v/webium.svg?maxAge=3600)](https://pypi.python.org/pypi/webium)
[![Python Versions](https://img.shields.io/pypi/pyversions/webium.svg?maxAge=3600)](https://pypi.python.org/pypi/webium)
[![Build Status](https://img.shields.io/travis/wgnet/webium/master.svg?maxAge=3600)](https://travis-ci.org/wgnet/webium)

Webium is a Page Object pattern implementation library for Python (http://martinfowler.com/bliki/PageObject.html).

It allows you to extend WebElement class to your custom controls like Link, Button and group them as pages.

## Installation

The latest stable version is available on PyPI:

    pip install webium

## Usage

Main classes are:

- webium.Find
- webium.Finds
- webium.BasePage

Basic usage example:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium.controls.link import Link
from webium.driver import get_driver
from webium import BasePage, Find, Finds


class GooglePage(BasePage):
    url = 'http://www.google.com'

    text_field = Find(by=By.NAME, value='q')
    button = Find(by=By.NAME, value='btnK')


class ResultItem(WebElement):
    link = Find(Link, By.XPATH, './/h3/a')


class ResultsPage(BasePage):
    stat = Find(by=By.ID, value='resultStats')
    results = Finds(ResultItem, By.XPATH, '//div/li')


if __name__ == '__main__':
    home_page = GooglePage()
    home_page.open()
    home_page.text_field.send_keys('Page Object')
    home_page.button.click()
    results_page = ResultsPage()
    print('Results summary: ' + results_page.stat.text)
    for item in results_page.results:
        print(item.link.text)
    get_driver().quit()
```

More usage details are available here: http://wgnet.github.io/webium/
