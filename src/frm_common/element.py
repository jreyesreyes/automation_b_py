from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElemDom:

    session = None
    name = None
    css_selector = None
    element = None

    def __init__(self, p_session, p_css, p_name=None):
        self.session = p_session
        self.name = p_name
        self.css_selector = p_css
        self.__set_element()

    # region ACTIONS
    def get_element(self):
        return self.element

    def is_displayed(self):
        try:
            self.element.is_displayed()
        except:
            return False

    def until(self, p_time=5):
        WebDriverWait(self.session, p_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.css_selector)))

    def click(self):
        self.element.click()

    def set(self, p_value):
        self.element.send_keys(p_value)
    # endregion

    # region PRIVATE
    def __set_element(self):
        try:
            self.element = self.session.find_element_by_css_selector(self.css_selector)
        except:
            self.element = None

    # endregion

