from selenium.webdriver.common.by import By


class MainPageLoc:
    login_loc = (By.CSS_SELECTOR, ".login")
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')
    add_basket = (By.XPATH, "//a[@data-id-product = '2']")
    go_basket = (By.XPATH, "//a[@title = 'View my shopping cart']")
    cross_loc = (By.XPATH, "//*[@class ='cross']")
    main_link_page = "http://automationpractice.com/index.php"


