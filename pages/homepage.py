from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    signin_button = (By.CSS_SELECTOR, "a[title='Log in to your customer account']")
    dresses_button = (By.XPATH, "(//a[@title='Dresses'])[2]")
    casual_dresses_button = (By.XPATH, "(//a[@title='Casual Dresses'])[2]")
    t_shirts_button = (By.XPATH, "(//a[@title='T-shirts'])[2]")

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.signin_button)
