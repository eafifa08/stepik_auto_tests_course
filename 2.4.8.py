from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def math_fun(x):
    return math.log(abs(12*math.sin(x)), math.e)


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element(By.ID, 'book')
locator = (By.ID, 'price')
text = '$100'
# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
price_el = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(locator, text))
button.click()

x_el = browser.find_element(By.ID, 'input_value')
x = int(x_el.text)
answer = str(math_fun(x))

answer_el = browser.find_element(By.ID, 'answer')
answer_el.send_keys(answer)


button_submit = browser.find_element(By.ID, "solve")
button_submit.click()

alert = browser.switch_to.alert
print(alert.text)
