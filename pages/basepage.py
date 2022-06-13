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

    # click on a element whenever the element is clickable
    def click_on(self, by_locator):
        self.wait.until(ec.element_to_be_clickable(by_locator)).click()

    # send_keys after presence of input element
    def send_text(self, by_locator, value):
        self.wait.until(ec.presence_of_element_located(by_locator)).send_keys(value)

    # Get element text after visibility of the element
    def get_text(self, by_locator):
        return self.wait.until(ec.visibility_of_element_located(by_locator)).text

    #  Check visibility of an element. Return true if element exist on the page, otherwise false
    def is_visible(self, by_locator):
        element = self.wait.until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    # Get title of current page
    def get_title(self, title):
        self.wait.until(ec.title_is(title))
        return self.driver.title

    # Get url of current page
    def get_url(self, url):
        self.wait.until(ec.url_to_be(url))
        return self.driver.current_url

    # Wait for a specific element to be visible on the web page
    def wait_for_element(self, by_locator):
        self.wait.until(ec.visibility_of_element_located(by_locator))

    # Wait for an alert to be present on the web page
    def wait_for_alert(self):
        return self.wait.until(ec.alert_is_present())

    # Get an element on the web page
    def get_element(self, by_locator):
        return self.wait.until(ec.presence_of_element_located(by_locator))

    #  Get list of elements on the web page
    def get_elements(self, by_locator):
        return self.wait.until(ec.presence_of_all_elements_located(by_locator))

    # Get the size of list of elements
    def get_count(self, by_locator):
        return len(self.get_elements(by_locator))

    # Handle Select and options tag related task
    # Select an items by its visible text
    def select_by_text(self, by_locator, option):
        select = Select(self.get_element(by_locator))
        select.select_by_visible_text(option)

    # Select an items by its value
    def select_by_value(self, by_locator, value):
        select = Select(self.get_element(by_locator))
        select.select_by_value(value)

    # Select an items by its index
    def select_by_index(self, by_locator, index):
        select = Select(self.get_element(by_locator))
        select.select_by_index(index)

    #  Get currently first selected items text
    def get_selected_item_text(self, by_locator):
        select = Select(self.get_element(by_locator))
        return select.first_selected_option.text

    # Handle List tag related task
    # Select/click on an items from a list by its index
    def select_from_list_by_index(self, by_locator, position):
        list_items = self.get_elements(by_locator)
        list_items[position - 1].click()

    # Select/click on an items from a list by its visible text
    def select_from_list_by_text(self, by_locator, text):
        list_items = self.get_elements(by_locator)
        for element in list_items:
            if element.text == text:
                element.click()
                break

    # Perform javascript related tasks
    # Click on a hidden element using javascript
    def click_on_using_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    # Click on a hidden element using javascript script
    def click_on_using_js_script(self, script):
        self.driver.execute_script(script + ".click();")

    # Scroll to an element
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Scroll to page scrollable height
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Scroll within an element by offset
    def scroll_inside_element(self, css_locator, offset_x, offset_y):
        self.driver.execute_script("document.querySelector('" + css_locator + "').scrollBy(" + offset_x + "," + offset_y + ");")

    # Highlight an element by drawing a red rectangle around the element
    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style','border:2px solid red;background: beige');", element)

    # Perform Action chain related tasks
    # Perform drag and drop from one element to another element.
    def drag_and_drop_by_element(self, source_element, target_element):
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    # Perform smooth drag and drop from one element to another element with delay.
    def drag_and_drop_by_element_delay(self, source_element, target_element, delay):
        action = ActionChains(self.driver)
        action.click_and_hold(source_element).pause(delay).move_to_element(target_element).perform()

    # Perform drag and drop by offset.
    def drag_and_drop_by_offset(self, source_element, offset_x, offset_y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source_element, offset_x, offset_y).perform()

    # Perform hover on an element
    def hover_on_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    # Perform hover and click on an element
    def hover_on_element_and_click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    # Find an element within of a Shadow DOM
    def find_element_within_shadow_dom(self, host_element, by_locator):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', host_element)
        return shadow_root.find_element(by_locator)

    # Handle alert related tasks
    # Accept an alert
    def alert_accept(self):
        self.wait_for_alert().accept()

    # Write within an alert and accept the alert
    def alert_accept_with_send_text(self, text):
        alert = self.wait_for_alert().send_keys(text)
        alert.accept()

    # Dismiss or Cancel an alert
    def alert_dismiss(self):
        self.wait_for_alert().dismiss()

    # Get alert text
    def alert_text(self):
        return self.wait_for_alert().text

    # Switch to iframe when it's available
    def switch_to_iframe(self, name_or_id_or_element):
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(name_or_id_or_element))

