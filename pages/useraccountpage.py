from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from test_data.config import TestData


class UserAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    sign_out_Button = (By.CSS_SELECTOR, "a[title='Log me out']")
    account_name = (By.CSS_SELECTOR, "a[title='View my customer account'] span")

    def get_user_account_page_title(self, title):
        return self.get_title(title)

    def get_account_name_text(self):
        return self.get_text(self.account_name)
    
