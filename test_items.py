import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_looking_for_add_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    buttons = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert buttons == 1, "Неверный селектор или такой кнопки не существует"
