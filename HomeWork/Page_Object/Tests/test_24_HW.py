import pytest

from HomeWork.Page_Object.Pages.login_page import LoginPage
from HomeWork.Page_Object.Pages.main_page import MainPage
from HomeWork.Page_Object.Pages.basket_page import BasketPage
import time
from selenium import webdriver


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('chromedriver.exe')
    browser.implicitly_wait(5)


def test_guest_can_open_login_page(open_browser):
    link = "http://automationpractice.com/index.php"
    page = MainPage(browser, link)

    try:
        page.open()
        page.verify_login_link()
        page.open_login_page()
        login_page = LoginPage(browser, url=browser.current_url)
        login_page.verify_login_link()
    finally:
        browser.quit()


def test_basket_is_empty(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.verify_basket_is_empty()
    finally:
        browser.quit()


def test_main_page(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.verify_add_to_basket()
        main_page.close_field_with_add_thing()
        main_page.go_to_basket_page()
        main_page.verify_item_basket()
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.verify_main_link_page()
    finally:
        time.sleep(3)
        browser.quit()


def test_basket_page(open_browser):
    link = "http://automationpractice.com/index.php?controller=order"
    basket_page = BasketPage(browser, link)

    try:
        basket_page.open()
        basket_page = BasketPage(browser, link)
        basket_page.verify_basket_link_page()
    finally:
        time.sleep(3)
        browser.quit()


def test_pages(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.go_to_basket_page()
        main_page.verify_basket_is_empty()
    finally:
        time.sleep(3)
        browser.quit()


def test_pages2(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.open_login_page()
        main_page.verify_login_link()
        login_page = LoginPage(browser, url=browser.current_url)
        login_page.verify_login_link()
    finally:
        time.sleep(3)
        browser.quit()
