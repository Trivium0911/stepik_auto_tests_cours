from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    num = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer = calc(num.text)
    answer_pole = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_pole.send_keys(answer)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
