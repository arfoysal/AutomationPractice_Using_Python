from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.useraccountpage import UserAccountPage
from test_data.config import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.LOGIN_PAGE_URL)

    signin_link = (By.CSS_SELECTOR, "a[title='Log in to your customer account']")
    create_account_email = (By.ID, "email_create")
    create_account_button = (By.ID, "SubmitCreate")
    login_email = (By.ID, "email")
    login_password = (By.ID, "passwd")
    login_button =(By.ID, "SubmitLogin")
    forgot_password_link = (By.LINK_TEXT, "Forgot your password?")

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.signin_link)

    def enter_email_address(self, email):
        self.send_text(self.login_email, email)

    def enter_password(self, password):
        self.send_text(self.login_password, password)

    def click_on_login_button(self):
        self.click_on(self.login_button)

    def if_forget_password_link_visible(self):
        self.is_visible(self.forgot_password_link)

    def create_account(self, email):
        self.send_text(self.create_account_email)
        self.click_on(self.create_account_button)

    def do_login(self, email, password):
        self.scroll_to_bottom()
        login_btn = self.get_element(self.login_button)
        self.scroll_to_element(login_btn)
        self.send_text(self.login_email, email)
        self.send_text(self.login_password, password)
        self.click_on(self.login_button)
        return UserAccountPage(self.driver)
