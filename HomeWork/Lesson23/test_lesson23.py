from selenium import webdriver
from selenium.webdriver.common.by import By


def test_input():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(5)  # неявное ожидание вместо sleep
    chrome.get('http://the-internet.herokuapp.com/dynamic_controls')
    try:
        chrome.maximize_window()
        chrome.find_element(By.XPATH, "//input[@type = 'checkbox']").click()
        chrome.find_element(By.XPATH, "//button[@onclick = 'swapCheckbox()']").click()
        check_message = chrome.find_element(By.XPATH, "//p[@id = 'message']").text
        assert check_message == "It's gone!"
        if len(chrome.find_elements(By.XPATH, "//*[@id='checkbox']")) != 0:
            print('Checkbox found.')
        else:
            print('Checkbox is not found.')

        element = chrome.find_element(By.XPATH, '//input')
        print(f' Input is enabled before click = {element.is_enabled()}')

        chrome.find_element(By.XPATH, "//button[@onclick = 'swapInput()']").click()
        check_message_2 = chrome.find_element(By.XPATH, "//p[@id = 'message']").text
        assert check_message_2 == "It's enabled!"

        element = chrome.find_element(By.XPATH, '//input')
        print(f' Input is enabled after click = {element.is_enabled()}')  # метод для проверки на enabled
    finally:
        chrome.quit()


def test_frames():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(5)  # неявное ожидание вместо sleep
    chrome.get('http://the-internet.herokuapp.com/frames')
    try:
        chrome.maximize_window()
        chrome.find_element(By.XPATH, "//a[@href = '/iframe']").click()
        chrome.switch_to.frame(chrome.find_element(By.ID, 'mce_0_ifr'))
        check_message = chrome.find_element(By.XPATH, "//body[@id = 'tinymce']").text
        assert check_message == 'Your content goes here.'

    finally:
        chrome.quit()
