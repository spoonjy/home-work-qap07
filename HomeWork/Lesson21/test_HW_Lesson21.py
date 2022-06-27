from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_demoqa_search_field1():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://demoqa.com/select-menu'
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(1)
        select_value = chrome.find_element(By.CLASS_NAME, 'css-1wy0on6').click()
        select_option = chrome.find_element(By.ID, 'react-select-2-option-0-0').click()
        selcect_one = chrome.find_element(By.CLASS_NAME, 'css-yk16xz-control').click()
        select_title = chrome.find_element(By.ID, 'react-select-3-option-0-1').click()
        old_style_menu = Select(chrome.find_element(By.ID, 'oldSelectMenu'))
        old_style_menu.select_by_value('10')
        multiselect = chrome.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div').click()
        multiselect_color = chrome.find_element(By.ID, 'react-select-4-option-1').click()
        multiselect_color = chrome.find_element(By.ID, 'react-select-4-option-2').click()
        multiselect_color = chrome.find_element(By.ID, 'react-select-4-option-0').click()
        multiselect_color = chrome.find_element(By.ID, 'react-select-4-option-3').click()
        time.sleep(5)
    finally:
        chrome.quit()


def test_demoqa_search_field2():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://demo.guru99.com/test/newtours/register.php'
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(1)
        #  Contact Information
        name = chrome.find_element(By.NAME, 'firstName').send_keys('Yaroslav')
        lastname = chrome.find_element(By.NAME, 'lastName').send_keys('Lukashevich')
        phone = chrome.find_element(By.NAME, 'phone').send_keys('123456789')
        email = chrome.find_element(By.NAME, 'userName').send_keys('YL@gmail.com')

        # Mailing Information
        address = chrome.find_element(By.NAME, 'address1').send_keys('Winnie the Pooh Street')
        city = chrome.find_element(By.NAME, 'city').send_keys('Warsaw')
        state = chrome.find_element(By.NAME, 'state').send_keys('Warsaw')
        postal_code = chrome.find_element(By.NAME, 'postalCode').send_keys('2500025')
        country = Select(chrome.find_element(By.NAME, 'country'))
        country.select_by_visible_text('POLAND')

        #   User Information
        user_name = chrome.find_element(By.NAME, 'email').send_keys('Yar90q')
        password = chrome.find_element(By.NAME, 'password').send_keys('123123123')
        confirm_password = chrome.find_element(By.NAME, 'confirmPassword').send_keys('123123123')

        time.sleep(5)
        button = chrome.find_element(By.NAME, 'submit').click()
        time.sleep(3)

        verify_name = chrome.find_element(By.XPATH,
                                          '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b').text
        verify_user_name = chrome.find_element(By.XPATH,
                                               '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b').text
        assert 'Dear Yaroslav Lukashevich,' == verify_name
        assert 'Note: Your user name is Yar90q.' == verify_user_name
    finally:
        chrome.quit()
