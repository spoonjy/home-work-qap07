import pytest
from selenium import webdriver
from HomeWork.Page_Object.Pages.main_page import MainPage
from HomeWork.Page_Object.Pages.basket_page import BasketPage
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('./test_bdd_page.feature')


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('chromedriver.exe')
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@given('We are opening main page')
def open_site(open_browser):
    link = "http://automationpractice.com/index.php"
    global main_page
    main_page = MainPage(open_browser, link)
    main_page.open()


@when('We are opening basket page')
def open_basket_page():
    main_page.open_basket_page()


@then('We are verifying basket page')
def verify_basket_page():
    basket_page = BasketPage(browser, url=browser.current_url)
    basket_page.verify_basket_link_page()
