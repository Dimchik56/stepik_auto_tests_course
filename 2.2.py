import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.ID, "button")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element(By.TAG_NAME, "button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value").text
    x = str(x_element)

    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer").send_keys(y)

    submit = browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(5)
    browser.quit()

