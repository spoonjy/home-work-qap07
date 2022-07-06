from selenium.webdriver.common.by import By


class BasketPageLoc:
    basket_item_loc = (By.XPATH, "//p/a[text()='Blouse']")
    basket_link_page = "http://automationpractice.com/index.php?controller=order"
