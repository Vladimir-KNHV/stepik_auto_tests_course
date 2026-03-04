from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, 'book').click()
    browser.execute_script("window.scrollBy(0, 100);")
    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input2 = browser.find_element(By.ID, 'answer').send_keys(y)

    input3 = browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    browser.quit()



