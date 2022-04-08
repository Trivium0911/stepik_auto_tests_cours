from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")
    number = number_elem.text
    answer = calc(number)
    answer_pole = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_pole.send_keys(answer)
    check_rob = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_rob.click()
    rob_rul = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rob_rul.click()
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
