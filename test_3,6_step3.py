import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    mas = ['https://stepik.org/lesson/236895/step/1',
           'https://stepik.org/lesson/236896/step/1',
           'https://stepik.org/lesson/236897/step/1',
           'https://stepik.org/lesson/236898/step/1',
           'https://stepik.org/lesson/236899/step/1',
           'https://stepik.org/lesson/236903/step/1',
           'https://stepik.org/lesson/236904/step/1',
           'https://stepik.org/lesson/236905/step/1]']
    res = ''

    @pytest.mark.parametrize('links', mas)
    def test_func(self, browser, links):

        browser.get(str(links))
        browser.implicitly_wait(30)
        pole = browser.find_element(By.TAG_NAME, 'textarea')
        pole.send_keys(str(math.log(int(time.time()))))
        btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        btn.click()
        cor = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text
        assert cor == "Correct!", f'Error: {cor}'

if __name__ == "__main__":
    pytest.main()