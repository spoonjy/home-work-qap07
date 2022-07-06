from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url

    def open(self):
        self.chrome.get(self.url)

    def is_element_present(self, locator):  # проверка присутствия на странице
        try:
            self.chrome.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
