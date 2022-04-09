from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_first = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    element_first.send_keys("Пиво")
    element_second = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    element_second.send_keys("Пиво")
    element_mail = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    element_mail.send_keys("Пиво")
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "body > div > h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
