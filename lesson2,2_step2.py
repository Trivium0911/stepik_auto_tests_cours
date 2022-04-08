from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_num = browser.find_element(By.CSS_SELECTOR, "#num1")
    second_num = browser.find_element(By.CSS_SELECTOR, "#num2")
    summ  = int(first_num.text) + int(second_num.text)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text(str(summ))
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
