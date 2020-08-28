from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.expedia.com/")
print(driver.current_url)
print(driver.title)
assert "Expedia" in driver.title

css_selector = "button[data-stid='location-field-destination-menu-trigger']"

# Wait until 'going to' is displayed
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

# Click on 'going to'
obj = driver.find_element_by_css_selector(css_selector)
obj.click()

driver.close()




