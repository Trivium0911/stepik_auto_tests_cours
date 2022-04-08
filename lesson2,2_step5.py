from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer = calc(number.text)
    answer_pole = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_pole.send_keys(answer)
    check_rob = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.form-check.form-check-custom > label")
    check_rob.click()
    rob_rul = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.form-check.form-radio-custom > label")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rob_rul)
    rob_rul.click()
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()