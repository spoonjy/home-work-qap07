from selenium.webdriver.common.by import By


class ContactPageLoc:
    contact_link_loc = (By.XPATH, "//a[@title='Contact Us']")
    contact_text = (By.XPATH, "//h1[@class = 'page-heading bottom-indent']")

