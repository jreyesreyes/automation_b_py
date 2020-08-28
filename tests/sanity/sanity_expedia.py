from src.frm_common.browser import Browser
from src.frm_expedia.repository.homepage import HomePage
from selenium.webdriver.common.keys import Keys

try:
    b = Browser('chrome', 'https://expedia.com/')
    b.open()
    print(b.current_url())
    print(b.title())
    assert "Expedia" in b.title()

    h = HomePage(b.driver)
    h.going_to.click()
    h.going_to_input.set("Paris")
    h.going_to_input.set(Keys.ENTER)

    # Click on Search
    h.search.click()
finally:
    b.close()