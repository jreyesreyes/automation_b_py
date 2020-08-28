from src.frm_common.element import ElemDom
from selenium.webdriver.common.by import By


class HomePage:

    driver = None

    def __init__(self, p_driver):
        self.driver = p_driver

    @property
    def going_to(self):
        css_selector = "button[data-stid='location-field-destination-menu-trigger']"
        return ElemDom(self.driver, css_selector, 'Going To')

    @property
    def going_to_input(self):
        css_selector = "input[data-stid='location-field-destination-menu-input']"
        return ElemDom(self.driver, css_selector, 'Going To - Input')

    @property
    def lst_going_to(self):
        css_selector = "li[data-stid='location-field-destination-result-item']"
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)

    @property
    def search(self):
        css_selector = "button[data-testid='submit-button'][type='submit']"
        return ElemDom(self.driver, css_selector, 'Search')
