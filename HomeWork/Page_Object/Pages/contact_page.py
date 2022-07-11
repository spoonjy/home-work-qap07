from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from HomeWork.Page_Object.Locators.contact_locators import ContactPageLoc
from HomeWork.Page_Object.Pages.base_page import BasePage
import time


class ContactPage(BasePage):
    def open_contact_page(self):
        time.sleep(2)
        open_contact = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(ContactPageLoc.contact_link_loc))
        open_contact.click()

    def verify_text(self):
        assert self.is_element_present(ContactPageLoc.contact_text)
