from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_ultimateqa_com_click():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://ultimateqa.com/complicated-page/'
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(1)
        chrome.find_element(By.XPATH, "//a[@class ='et_pb_button et_pb_button_4 et_pb_bg_layout_light']").click()
        chrome.find_element(By.CSS_SELECTOR, 'a.et_pb_button.et_pb_button_4.et_pb_bg_layout_light').click()
        chrome.find_element(By.CLASS_NAME, 'et_pb_button, et_pb_button_4, et_pb_bg_layout_light').click()
        time.sleep(3)
    finally:
        chrome.quit()


def test_ultimateqa_com_full():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(1)
        chrome.find_element(By.XPATH, "//input[@id = 'et_pb_contact_name_0']").send_keys('Yaroslav')
        chrome.find_element(By.XPATH, "//textarea[@name = 'et_pb_contact_message_0']").send_keys('learning xpath :)')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        time.sleep(3)
        chrome.find_element(By.XPATH, "//div/p[text() = 'Thanks for contacting us']")
    finally:
        chrome.quit()


# Выше я сделал без assert, а ниже с ним, просто, чтобы были разные варианты)

def test_ultimateqa_com_name():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.maximize_window()
        chrome.find_element(By.XPATH, "//input[@id = 'et_pb_contact_name_0']").send_keys('Yaroslav')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        time.sleep(3)
        check_for_error_name = chrome.find_element(By.XPATH, '//div/p').text
        assert 'Make sure you fill in all required fields.' == check_for_error_name
    finally:
        chrome.quit()


def test_ultimateqa_com_message():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.maximize_window()
        chrome.find_element(By.XPATH, "//textarea[@name = 'et_pb_contact_message_0']").send_keys(
            'learning xpath more :)')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        time.sleep(3)
        check_for_error_message = chrome.find_element(By.XPATH, '//div/p').text
        assert 'Make sure you fill in all required fields.' == check_for_error_message
    finally:
        chrome.quit()
