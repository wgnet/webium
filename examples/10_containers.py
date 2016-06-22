from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds, BasePage


class Vacancy(WebElement):
    title = Find(by=By.CLASS_NAME, value='vacancy_title')
    profession = Find(by=By.CLASS_NAME, value='vacancy_profession')
    location = Find(by=By.CLASS_NAME, value='vacancy_location')
    apply_button = Find(by=By.CLASS_NAME, value='vacancy_apply_button')


class VacanciesPage(BasePage):
    vacancies_list = Finds(Vacancy, By.XPATH, '//div[@id="careers-vacancies"]/div[@data-id]')

    def __init__(self):
        super(VacanciesPage, self).__init__(url='http://wargaming.com/en/careers/vacancies/')


if __name__ == '__main__':
    page = VacanciesPage()
    page.open()
    for vacancy in page.vacancies_list:
        # search by CLASS_NAME='vacancy_title' is performed within one node
        print('Title: ' + vacancy.title.text)
