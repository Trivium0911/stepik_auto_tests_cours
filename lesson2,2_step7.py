from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'abc.txt')
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements(By.CLASS_NAME, "form-control")
    for element in elements:
        element.send_keys("Пиво")
    elem = browser.find_element(By.CSS_SELECTOR, "#file")
    elem.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

