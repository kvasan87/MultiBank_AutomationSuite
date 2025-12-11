from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utils.logger import log_debug, log_error
import time


class WaitHelper:
    """Helper class for Selenium waits with custom conditions"""

    DEFAULT_TIMEOUT = 10
    SHORT_TIMEOUT = 5
    LONG_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def wait_for_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for element to be visible"""
        try:
            log_debug(f"Waiting for element visible: {locator}")
            element = WebDriverWait(
                self.driver, timeout
            ).until(
                EC.visibility_of_element_located(locator)
            )
            log_debug(f"Element found and visible: {locator}")
            return element
        except TimeoutException:
            log_error(f"Element not visible within {timeout}s: {locator}")
            raise

    def wait_for_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for element to be clickable"""
        try:
            log_debug(f"Waiting for element clickable: {locator}")
            element = WebDriverWait(
                self.driver, timeout
            ).until(
                EC.element_to_be_clickable(locator)
            )
            log_debug(f"Element clickable: {locator}")
            return element
        except TimeoutException:
            log_error(f"Element not clickable within {timeout}s: {locator}")
            raise

    def wait_for_elements_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for multiple elements to be visible"""
        try:
            log_debug(f"Waiting for elements visible: {locator}")
            elements = WebDriverWait(
                self.driver, timeout
            ).until(
                EC.presence_of_all_elements_located(locator)
            )
            log_debug(f"Elements found: {locator}")
            return elements
        except TimeoutException:
            log_error(f"Elements not visible within {timeout}s: {locator}")
            raise

    def wait_for_element_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for element to become invisible"""
        try:
            log_debug(f"Waiting for element invisible: {locator}")
            WebDriverWait(
                self.driver, timeout
            ).until(
                EC.invisibility_of_element_located(locator)
            )
            log_debug(f"Element is now invisible: {locator}")
        except TimeoutException:
            log_error(f"Element still visible after {timeout}s: {locator}")
            raise

    def wait_for_text_in_element(self, locator, text, timeout=DEFAULT_TIMEOUT):
        """Wait for specific text in element"""
        try:
            log_debug(f"Waiting for text '{text}' in element: {locator}")
            WebDriverWait(
                self.driver, timeout
            ).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            log_debug(f"Text found in element: {locator}")
        except TimeoutException:
            log_error(f"Text '{text}' not found in {timeout}s: {locator}")
            raise

    def wait_for_url_contains(self, url_substring, timeout=DEFAULT_TIMEOUT):
        """Wait for URL to contain substring"""
        try:
            log_debug(f"Waiting for URL to contain: {url_substring}")
            WebDriverWait(
                self.driver, timeout
            ).until(
                EC.url_contains(url_substring)
            )
            log_debug(f"URL contains: {url_substring}")
        except TimeoutException:
            log_error(f"URL does not contain '{url_substring}' after {timeout}s")
            raise

    def wait_for_url_changes(self, original_url, timeout=DEFAULT_TIMEOUT):
        """Wait for URL to change from original"""
        try:
            log_debug(f"Waiting for URL to change from: {original_url}")
            WebDriverWait(
                self.driver, timeout
            ).until(
                lambda driver: driver.current_url != original_url
            )
            log_debug(f"URL changed to: {self.driver.current_url}")
        except TimeoutException:
            log_error(f"URL did not change within {timeout}s")
            raise

    def wait_for_element_attribute(self, locator, attribute, value, timeout=DEFAULT_TIMEOUT):
        """Wait for element attribute to have specific value"""
        try:
            log_debug(f"Waiting for {attribute}='{value}' on: {locator}")
            WebDriverWait(
                self.driver, timeout
            ).until(
                lambda driver: driver.find_element(*locator).get_attribute(attribute) == value
            )
            log_debug(f"Element attribute matched: {locator}")
        except TimeoutException:
            log_error(f"Element attribute not matched within {timeout}s: {locator}")
            raise

    def wait_for_ajax_complete(self, timeout=DEFAULT_TIMEOUT):
        """Wait for jQuery AJAX to complete"""
        try:
            log_debug("Waiting for AJAX to complete...")
            WebDriverWait(
                self.driver, timeout
            ).until(
                lambda driver: driver.execute_script("return jQuery.active == 0")
            )
            log_debug("AJAX completed")
        except Exception as e:
            log_error(f"AJAX wait failed: {str(e)}")

    def wait_for_page_load(self, timeout=DEFAULT_TIMEOUT):
        """Wait for page to fully load"""
        try:
            log_debug("Waiting for page load...")
            WebDriverWait(
                self.driver, timeout
            ).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            log_debug("Page fully loaded")
        except TimeoutException:
            log_error(f"Page did not fully load within {timeout}s")
            raise

    def element_exists(self, locator, timeout=SHORT_TIMEOUT):
        """Check if element exists without throwing exception"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def element_is_displayed(self, locator, timeout=SHORT_TIMEOUT):
        """Check if element is displayed"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False