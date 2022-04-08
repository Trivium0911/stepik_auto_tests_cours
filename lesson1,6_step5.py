import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"


try:
    driver = webdriver.Chrome()
    driver.get(link)
    lnk =driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    lnk.click()

    input1 = driver.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
        # успеваем скопировать код за 30 секунд
    time.sleep(30)
        # закрываем браузер после всех манипуляций
    driver.quit()

    # не забываем оставить пустую строку в конце файла