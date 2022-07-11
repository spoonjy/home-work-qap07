from HomeWork.Page_Object.Locators.basket_locators import BasketPageLoc
from HomeWork.Page_Object.Pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from HomeWork.Page_Object.Locators.main_locators import MainPageLoc

basket_link = "http://automationpractice.com/index.php?controller=order"


class BasketPage(BasePage):

    def verify_item_basket(self):
        assert self.is_element_present(BasketPageLoc.basket_item_loc)

    # проверка на присутствие элемента на странице
    # в данном случае это тайтл страницы
    def verify_basket_title(self):
        assert self.is_element_present(BasketPageLoc.title_basket)

    # проверка на соответствие ссылки и вывод сообщения в случае ошибки
    def verify_basket_link_page(self):
        basket_link_page = self.chrome.current_url
        assert basket_link_page == basket_link, 'The url page does not match'
