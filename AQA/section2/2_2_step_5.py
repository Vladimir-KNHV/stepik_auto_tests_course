from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")

# СКРОЛИМ СТРАНИЦУ
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
# ТОЖЕ СКРОЛИМ
browser.execute_script("window.scrollBy(0, 100);")