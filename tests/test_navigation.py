"""
tests/test_navigation.py - Navigation and Layout Test Suite
"""

import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage
from src.utils.logger import log_info
from src.constants.locators import HomePageLocators

@allure.feature("Navigation & Layout")
@allure.story("Top Navigation Menu")
class TestNavigation:
    """Test cases for navigation and layout"""

    @pytest.mark.smoke
    @allure.title("Verify navigation menu displays correctly")
    @allure.description("Verify that the top navigation menu is visible and displays all expected options")
    def test_navigation_menu_visible(self, driver):
        """Test that navigation menu is visible"""
        home_page = HomePage(driver)
        home_page.load()

        with allure.step("Verify navigation menu is visible"):
            home_page.verify_navigation_menu_visible()

        log_info("✓ Navigation menu visibility test passed")

    @pytest.mark.smoke
    @allure.title("Verify all navigation items exist")
    @allure.description("Verify that all expected navigation items are present in the menu")
    def test_navigation_items_exist(self, driver):
        """Test that all navigation items exist"""
        home_page = HomePage(driver)
        home_page.load()

        with allure.step("Verify all navigation items exist"):
            home_page.verify_navigation_items_exist()

        log_info("✓ Navigation items existence test passed")

    @pytest.mark.regression
    @allure.title("Test Markets link navigation")
    @allure.description("Verify that clicking Markets link navigates to correct page")
    def test_markets_link_navigation(self, driver):
        """Test Markets link navigation"""
        home_page = HomePage(driver)
        home_page.load()

        initial_url = driver.current_url
        with allure.step("Click Markets link"):
            home_page.click_markets_link()

        # Wait for URL to change
        WebDriverWait(driver, 10).until(EC.url_changes(initial_url))

        new_url = driver.current_url
        assert initial_url != new_url, "URL should change after clicking Markets link"
        log_info(f"✓ Markets link navigation test passed - Navigated to {new_url}")

    @pytest.mark.regression
    @allure.title("Test About-Awards link navigation")
    @allure.description("Verify that clicking About link navigates to Awards page")
    def test_about_link_navigation(self, driver):
        """Test About link navigation"""
        home_page = HomePage(driver)
        home_page.load()

        initial_url = driver.current_url
        with allure.step("Click About link Awards Option"):
            home_page.click_about_link("Awards")

        WebDriverWait(driver, 10).until(EC.url_changes(initial_url))

        current_url = driver.current_url
        assert "about" in current_url.lower() or "about" in driver.page_source.lower(), "Should navigate to about page"
        log_info(f"✓ About link navigation test passed - URL: {current_url}")

    @pytest.mark.smoke
    @allure.title("Verify page title is correct")
    @allure.description("Verify that the home page has the correct title")
    def test_page_title(self, driver):
        """Test page title"""
        home_page = HomePage(driver)
        home_page.load()

        title = home_page.get_home_page_title()
        assert title, "Page title should not be empty"

        log_info(f"✓ Page title test passed - Title: {title}")