import pytest
import allure
from src.pages.home_page import HomePage
from src.pages.about_page import AboutPage
from src.pages.why_multilink_page import WhyMultilinkPage
from src.utils.logger import log_info
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage

@allure.feature("Content Validation")
@allure.story("Marketing Banners and Downloads")
class TestContentValidation:
    """Test cases for content validation"""

    @pytest.mark.smoke
    @allure.title("Verify marketing banners appear at bottom")
    @allure.description("Verify that marketing banners are visible at the bottom of the home page")
    def test_marketing_banners_visible(self, driver):
        """Test that marketing banners are visible"""
        home_page = HomePage(driver)
        home_page.load()

        with allure.step("Verify marketing banners are visible"):
            home_page.verify_marketing_banners_visible()

        banners_count = home_page.get_marketing_banners_count()
        log_info(f"✓ Marketing banners test passed - Found {banners_count} banners")

    @pytest.mark.regression
    @allure.title("Verify download section is visible")
    @allure.description("Verify that the download section appears and is accessible")
    def test_download_section_visible(self, driver):
        """Test that download section is visible"""
        home_page = HomePage(driver)
        home_page.load()

        with allure.step("Verify download section is visible"):
            home_page.verify_download_section_visible()

        log_info("✓ Download section visibility test passed")

    @pytest.mark.smoke
    @allure.title("Verify App Store link exists")
    @allure.description("Verify that App Store download link is present and functional")
    def test_app_store_link_exists(self, driver):
        """Test that App Store link exists"""
        home_page = HomePage(driver)
        home_page.load()

        with allure.step("Verify download section is visible"):
            home_page.verify_download_section_visible()

        with allure.step("Verify App Store link exists"):
            home_page.verify_app_store_link_exists()

        log_info("✓ App Store link existence test passed")

    @pytest.mark.smoke
    @allure.title("Verify Google Play link exists")
    @allure.description("Verify that Google Play download link is present and functional")
    def test_google_play_link_exists(self, driver):
        """Test that Google Play link exists"""
        home_page = HomePage(driver)
        home_page.load()

        with allure.step("Verify download section is visible"):
            home_page.verify_download_section_visible()

        with allure.step("Verify Google Play link exists"):
            home_page.verify_google_play_link_exists()

        log_info("✓ Google Play link existence test passed")

    @pytest.mark.regression
    @allure.title("Verify App Store link is clickable")
    @allure.description("Verify that App Store link can be clicked without errors")
    def test_app_store_link_clickable(self, driver):
        """Test that App Store link is clickable"""
        home_page = HomePage(driver)
        home_page.load()

        home_page.verify_download_section_visible()

        with allure.step("Click App Store link"):
            original_window = home_page.click_app_store_link()

        log_info("✓ App Store link clickable test passed")

    @pytest.mark.regression
    @allure.title("Verify Google Play link is clickable")
    @allure.description("Verify that Google Play link can be clicked without errors")
    def test_google_play_link_clickable(self, driver):
        """Test that Google Play link is clickable"""
        home_page = HomePage(driver)
        home_page.load()

        home_page.verify_download_section_visible()

        with allure.step("Click Google Play link"):
            original_window = home_page.click_google_play_link()

        log_info("✓ Google Play link clickable test passed")

    @pytest.mark.regression
    @allure.title("Verify Why why-multibank page renders correctly")
    @allure.description("Verify that Why why-multibank page renders with all expected components")
    def test_why_multilink_page_renders(self, driver):
        """Test that Why MultiLink page renders"""
        home_page = HomePage(driver)
        home_page.load()

        initial_url = driver.current_url
        with allure.step("Click About link Awards Option"):
            home_page.click_about_link("WhyMultiBank")

        WebDriverWait(driver, 10).until(EC.url_changes(initial_url))

        current_url = driver.current_url
        assert "why-multibank" in current_url.lower() or "why-multibank" in driver.page_source.lower(), "Should navigate to why-multibank page"
        log_info(f"✓ why-multibank link navigation test passed - URL: {current_url}")
