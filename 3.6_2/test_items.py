import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_basket_avalible(browser, languages):
    link = f"http://selenium1py.pythonanywhere.com/{languages}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    
    assert basket.get_attribute('class') == "btn btn-lg btn-primary btn-add-to-basket", "basket not find!"
