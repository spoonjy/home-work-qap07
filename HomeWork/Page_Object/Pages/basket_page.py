from HomeWork.Page_Object.Locators.basket_locators import BasketPageLoc
from HomeWork.Page_Object.Pages.base_page import BasePage


class BasketPage(BasePage):
    def verify_basket_link_page(self):
        basket_link_page = self.chrome.current_url
        assert basket_link_page == BasketPageLoc.basket_link_page
