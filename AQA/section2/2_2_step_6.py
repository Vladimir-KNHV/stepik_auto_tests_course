from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    browser.execute_script("window.scrollBy(0,100);")

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    input1 = browser.find_element(By.ID, 'robotCheckbox')
    input1.click()

    input1 = browser.find_element(By.ID, 'robotsRule')
    input1.click()

    input1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    input1.click()

finally:
    time.sleep(10)
    browser.quit()



