import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from HomeWork.Page_Object.Pages.base_page import BasePage
from HomeWork.Page_Object.Locators.main_locators import MainPageLoc
from HomeWork.Page_Object.Locators.basket_locators import BasketPageLoc


class MainPage(BasePage):

    def open_login_page(self):
        time.sleep(3)
        open_login = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.login_loc))
        open_login.click()

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Element is absent!"

    def verify_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def add_basket(self):
        basket_link = self.chrome.find_element(MainPageLoc.add_basket)
        basket_link.click()

    def verify_add_to_basket(self):
        time.sleep(3)
        basket_link = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.add_basket))
        basket_link.click()

    def go_to_basket_page(self):
        time.sleep(3)
        go_to_basket_link = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.go_basket))
        go_to_basket_link.click()

    def close_field_with_add_thing(self):
        time.sleep(3)
        close_field = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.cross_loc))
        close_field.click()

    def verify_go_basket(self):
        assert self.is_element_present(MainPageLoc.go_basket)

    def verify_item_basket(self):
        assert self.is_element_present(BasketPageLoc.basket_item_loc)

    def verify_main_link_page(self):
        main_link_page = self.chrome.current_url
        assert main_link_page == MainPageLoc.main_link_page
