from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""This class is the parent of all pages"""
"""It contents all the generic methods related to page object"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click_on(self, by_locator):
        self.wait.until(ec.element_to_be_clickable(by_locator)).click()

    def send_text(self, by_locator, value):
        self.wait.until(ec.presence_of_element_located(by_locator)).send_keys(value)

    def get_text(self, by_locator):
        return self.wait.until(ec.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        element = self.wait.until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        self.wait.until(ec.title_is(title))
        return self.driver.title

    def get_url(self, url):
        self.wait.until(ec.url_to_be(url))
        return self.driver.current_url

    def wait_for_element(self, by_locator):
        self.wait.until(ec.visibility_of_element_located(by_locator))

    def wait_for_alert(self):
        return self.wait.until(ec.alert_is_present())

    def get_count(self, by_locator):
        return len(self.wait.until(ec.presence_of_all_elements_located(by_locator)))

    def get_element(self, by_locator):
        return self.wait.until(ec.presence_of_element_located(by_locator))

    def get_elements(self, by_locator):
        return self.wait.until(ec.presence_of_all_elements_located(by_locator))

    def select_by_text(self, by_locator, option):
        select = Select(self.get_element(by_locator))
        select.select_by_visible_text(option)

    def select_by_value(self, by_locator, value):
        select = Select(self.get_element(by_locator))
        select.select_by_value(value)

    def select_by_index(self, by_locator, index):
        select = Select(self.get_element(by_locator))
        select.select_by_index(index)

    def get_selected_item_text(self, by_locator):
        select = Select(self.get_element(by_locator))
        return select.first_selected_option.text

    def select_from_list_by_index(self, by_locator, position):
        list_items = self.get_elements(by_locator)
        list_items[position - 1].click()

    def select_from_list_by_text(self, by_locator, text):
        list_items = self.get_elements(by_locator)
        for element in list_items:
            if element.text == text:
                element.click()
                break

    def click_on_using_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_using_js_script(self, script):
        self.driver.execute_script(script + ".click();")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_inside_element(self, css_locator, offset_x, offset_y):
        self.driver.execute_script("document.querySelector('" + css_locator + "').scrollBy(" + offset_x + "," + offset_y + ");")

    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style','border:2px solid red;background: beige');", element)

    def drag_and_drop_by_element(self, source_element, target_element):
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    def drag_and_drop_by_element_delay(self, source_element, target_element, delay):
        action = ActionChains(self.driver)
        action.click_and_hold(source_element).pause(delay).move_to_element(target_element).perform()

    def drag_and_drop_by_offset(self, source_element, offset_x, offset_y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source_element, offset_x, offset_y).perform()

    def hover_on_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def hover_on_element_and_click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def find_element_within_shadow_dome(self, host_element, by_locator):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', host_element)
        return shadow_root.find_element(by_locator)

    def alert_accept(self):
        self.wait_for_alert().accept()

    def alert_accept_with_send_text(self, text):
        alert = self.wait_for_alert().send_keys(text)
        alert.accept()

    def alert_dismiss(self):
        self.wait_for_alert().dismiss()

    def alert_text(self):
        return self.wait_for_alert().text

    def switch_to_iframe(self, name_or_id_or_element):
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(name_or_id_or_element))

