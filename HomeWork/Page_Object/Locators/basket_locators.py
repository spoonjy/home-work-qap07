from selenium.webdriver.common.by import By


class BasketPageLoc:
    basket_item_loc = (By.XPATH, "//p/a[text()='Blouse']")
    open_basket = (By.XPATH, "//a[@title = 'View my shopping cart']")
    title_basket = (By.XPATH, "//title[text() = 'Order - My Store']")
