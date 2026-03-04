from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, 'treasure')
    x = input1.get_attribute('valuex')
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(y)

    input3 = browser.find_element(By.ID, 'robotCheckbox')
    input3.click()

    input4 = browser.find_element(By.ID, 'robotsRule')
    input4.click()

    input4 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    input4.click()

finally:
    time.sleep(10)
    browser.quit()












