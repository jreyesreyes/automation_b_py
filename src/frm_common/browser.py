from selenium import webdriver


def get_driver(p_brow):
    if p_brow == 'chrome':
        return webdriver.Chrome()
    elif p_brow == 'firefox':
        return webdriver.Firefox()
    elif p_brow == 'safari':
        return webdriver.Safari()
    elif p_brow == 'opera':
        return webdriver.Opera()


class New:

    s_brow = ''
    s_url = ''
    driver = None

    def __init__(self, p_brow, p_url):
        self.s_brow = p_brow
        self.s_url = p_url

    def open(self):
        self.driver = get_driver(self.s_brow)
        self.driver.get(self.s_url)

    def close(self):
        self.driver.close()

    def go(self, p_url):
        self.driver.get(p_url)

    def current_url(self):
        return self.driver.current_url

    def title(self):
        return self.driver.title
