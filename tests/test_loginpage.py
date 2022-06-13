import pytest

from pages.loginpage import LoginPage
from test_data.config import TestData
from tests.basetest import BaseTest


class TestLogin(BaseTest):
    def test_signup_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        assert self.loginpage.is_signup_link_exist()

    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        actual_title = self.loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert actual_title == TestData.LOGIN_PAGE_TITLE

    @pytest.mark.login
    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_EMAIL, TestData.PASSWORD)
