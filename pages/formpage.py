from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.useraccountpage import UserAccountPage
from test_data.config import TestData


class FormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.FORMPAGE_URL)

    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    male = (By.ID, "gender-radio-1")
    female = (By.ID, "gender-radio-2")
    g_other = (By.ID, "gender-radio-3")
    mobile_number = (By.ID, "userNumber")
    date_root = (By.ID, "dateOfBirthInput")
    select_month = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    select_year = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    day_twelve = (By.XPATH, "(//div[contains(@class,'react-datepicker__day react-datepicker__day--0')]) [15]")
    subject = (By.CSS_SELECTOR, ".subjects-auto-complete__value-container")
    sports = (By.XPATH, "//label[normalize-space()='Sports']")
    reading = (By.XPATH, "//label[normalize-space()='Reading']")
    music = (By.XPATH, "//label[normalize-space()='Music']")
    current_address = (By.ID, "currentAddress")
    state = (By.XPATH, "//div[contains(text(),'Select State')]")
    city = (By.XPATH, "//div[contains(text(),'Select City')]")
    submit = (By.ID, "submit")
    result_data = (By.XPATH, "//td")

    def get_login_page_title(self, title):
        return self.get_title(title)

    def enter_first_name(self, f_name):
        self.send_text(self.first_name, f_name)

    def enter_last_name(self, l_name):
        self.send_text(self.last_name, l_name)

    def enter_email(self, email):
        self.send_text(self.email, email)

    def select_gender_as_mail(self):
        element = self.get_element(self.male)
        self.click_on_using_js(element)

    def enter_mobile_number(self, mob_number):
        self.send_text(self.mobile_number, mob_number)

    def enter_date_of_birth(self):
        pass

