import pytest

from pages.loginpage import LoginPage
from test_data.config import TestData
from tests.basetest import BaseTest


class TestUserAccountpage(BaseTest):
    def test_user_account_page_title(self):
        loginpage = LoginPage(self.driver)
        useraccountpage = loginpage.do_login(TestData.USER_EMAIL, TestData.PASSWORD)
        actual_title = useraccountpage.get_user_account_page_title(TestData.USER_ACCOUNT_PAGE_TITLE)
        assert actual_title == TestData.USER_ACCOUNT_PAGE_TITLE

    def test_user_account_name(self):
        loginpage = LoginPage(self.driver)
        useraccountpage = loginpage.do_login(TestData.USER_EMAIL, TestData.PASSWORD)
        assert useraccountpage.get_account_name_text() == TestData.USER_ACCOUNT_NAME
