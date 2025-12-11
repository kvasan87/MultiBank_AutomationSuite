from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.utils.logger import log_info, log_error, log_debug
from src.utils.wait_helpers import WaitHelper
import allure


class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        self.actions = ActionChains(driver)

    def get_page_title(self):
        """Get page title"""
        title = self.driver.title
        log_debug(f"Page title: {title}")
        return title

    def get_page_url(self):
        """Get current page URL"""
        url = self.driver.current_url
        log_debug(f"Current URL: {url}")
        return url

    def navigate_to_url(self, url):
        """Navigate to specific URL"""
        log_info(f"Navigating to URL: {url}")
        self.driver.get(url)
        self.wait.wait_for_page_load()

    def click_element(self, locator):
        """Click on element"""
        try:
            element = self.wait.wait_for_element_clickable(locator)
            element.click()
            log_info(f"Clicked element: {locator}")
        except Exception as e:
            log_error(f"Failed to click element {locator}: {str(e)}")
            raise

    def click_option(self, locator):
        """Click on element"""
        try:
            element = self.wait.wait_for_element_clickable(locator)
            element.click()
            log_info(f"Clicked element: {locator}")
        except Exception as e:
            log_error(f"Failed to click element {locator}: {str(e)}")
            raise

    def click_element_with_js(self, locator):
        """Click element using JavaScript"""
        try:
            element = self.wait.wait_for_element_visible(locator)
            self.driver.execute_script("arguments[0].click();", element)
            log_info(f"Clicked element with JS: {locator}")
        except Exception as e:
            log_error(f"Failed to click element with JS {locator}: {str(e)}")
            raise

    def input_text(self, locator, text, clear_first=True):
        """Input text in element"""
        try:
            element = self.wait.wait_for_element_visible(locator)
            if clear_first:
                element.clear()
            element.send_keys(text)
            log_info(f"Entered text '{text}' in element: {locator}")
        except Exception as e:
            log_error(f"Failed to input text in {locator}: {str(e)}")
            raise

    def get_element_text(self, locator):
        """Get element text"""
        try:
            element = self.wait.wait_for_element_visible(locator)
            text = element.text
            log_debug(f"Element text: {text}")
            return text
        except Exception as e:
            log_error(f"Failed to get text from {locator}: {str(e)}")
            raise

    def get_element_attribute(self, locator, attribute):
        """Get element attribute value"""
        try:
            element = self.wait.wait_for_element_visible(locator)
            value = element.get_attribute(attribute)
            log_debug(f"Element attribute {attribute}: {value}")
            return value
        except Exception as e:
            log_error(f"Failed to get attribute {attribute} from {locator}: {str(e)}")
            raise

    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible"""
        return self.wait.element_is_displayed(locator, timeout)

    def is_element_present(self, locator, timeout=5):
        """Check if element is present on page"""
        return self.wait.element_exists(locator, timeout)

    def get_elements(self, locator):
        """Get all elements matching locator"""
        try:
            elements = self.wait.wait_for_elements_visible(locator)
            log_info(f"Found {len(elements)} elements matching: {locator}")
            return elements
        except Exception as e:
            log_error(f"Failed to get elements {locator}: {str(e)}")
            raise

    def get_elements_count(self, locator):
        """Get count of elements matching locator"""
        try:
            elements = self.driver.find_elements(*locator)
            count = len(elements)
            log_info(f"Element count for {locator}: {count}")
            return count
        except Exception as e:
            log_error(f"Failed to get element count for {locator}: {str(e)}")
            return 0

    def scroll_to_element(self, locator):
        """Scroll to element"""
        try:
            element = self.wait.wait_for_element_visible(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            log_info(f"Scrolled to element: {locator}")
        except Exception as e:
            log_error(f"Failed to scroll to element {locator}: {str(e)}")
            raise

    def scroll_down(self, pixels=500):
        """Scroll down by number of pixels"""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        log_debug(f"Scrolled down by {pixels} pixels")

    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log_info("Scrolled to bottom of page")

    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")
        log_info("Scrolled to top of page")

    def hover_over_element(self, locator):
        """Hover over element"""
        try:
            element = self.wait.wait_for_element_visible(locator)
            self.actions.move_to_element(element).perform()
            log_info(f"Hovered over element: {locator}")
        except Exception as e:
            log_error(f"Failed to hover over element {locator}: {str(e)}")
            raise

    def wait_for_url_to_contain(self, url_substring, timeout=10):
        """Wait for URL to contain substring"""
        self.wait.wait_for_url_contains(url_substring, timeout)

    def switch_to_new_window(self):
        """Switch to newly opened window"""
        main_window = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        log_info("Switched to new window")
        return main_window

    def switch_to_window(self, window_handle):
        """Switch to specific window"""
        self.driver.switch_to.window(window_handle)
        log_info(f"Switched to window: {window_handle}")

    def close_current_window(self):
        """Close current window"""
        self.driver.close()
        log_info("Closed current window")

    def get_page_source(self):
        """Get page source"""
        return self.driver.page_source

    def take_screenshot(self, filename):
        """Take screenshot of page"""
        try:
            self.driver.save_screenshot(filename)
            log_info(f"Screenshot saved: {filename}")
            with allure.step(f"Screenshot: {filename}"):
                allure.attach.file(filename, name=filename,
                                   attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            log_error(f"Failed to take screenshot: {str(e)}")

    def refresh_page(self):
        """Refresh current page"""
        self.driver.refresh()
        self.wait.wait_for_page_load()
        log_info("Page refreshed")

    def go_back(self):
        """Navigate back"""
        self.driver.back()
        log_info("Navigated back")

    def go_forward(self):
        """Navigate forward"""
        self.driver.forward()
        log_info("Navigated forward")

    @allure.step("Verify element text: {text}")
    def verify_element_text(self, locator, expected_text):
        """Verify element contains expected text"""
        actual_text = self.get_element_text(locator)
        assert expected_text in actual_text, \
            f"Expected '{expected_text}' in '{actual_text}'"
        log_info(f"Text verification passed: {expected_text}")

    @allure.step("Verify element is visible")
    def verify_element_visible(self, locator):
        """Verify element is visible"""
        assert self.is_element_visible(locator), \
            f"Element not visible: {locator}"
        log_info(f"Element visibility verified: {locator}")

    @allure.step("Verify element is present")
    def verify_element_present(self, locator):
        """Verify element is present"""
        assert self.is_element_present(locator), \
            f"Element not present: {locator}"
        log_info(f"Element presence verified: {locator}")