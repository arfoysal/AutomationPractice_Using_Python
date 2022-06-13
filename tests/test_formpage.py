import pytest

from pages.formpage import FormPage
from test_data.config import TestData
from tests.basetest import BaseTest


class TestLogin(BaseTest):

    def test_form_page_title(self):
        self.formpage = FormPage(self.driver)
        actual_title = self.formpage.get_title(TestData.FORMPAGE_TITLE)
        assert actual_title == TestData.FORMPAGE_TITLE

    @pytest.mark.formsubmit
    def test_submit_form(self):
        self.formpage = FormPage(self.driver)
        self.formpage.enter_first_name(TestData.FIRT_NAME)
        self.formpage.enter_last_name(TestData.LAST_NAME)
        self.formpage.enter_email(TestData.EMAIL)
        self.formpage.select_gender_as_mail()

