from HomeWork.Page_Object.Pages.base_page import BasePage
from HomeWork.Page_Object.Locators.main_locators import MainPageLoc


class LoginPage(BasePage):

    def open_login_page(self):
        login_link = self.chrome.find_element(MainPageLoc.login_loc)
        login_link.click()

    # def verify_login_url(self):

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Element is absent!"
