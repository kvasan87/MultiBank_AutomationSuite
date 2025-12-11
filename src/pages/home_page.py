from src.pages.base_page import BasePage
from src.constants.locators import HomePageLocators
from src.utils.logger import log_info
import allure


class HomePage(BasePage):
    """Home Page Object for MultiBank Trading Platform"""

    PAGE_URL = "https://trade.multibank.io/"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Load home page"""
        with allure.step("Navigate to Home Page"):
            self.navigate_to_url(self.PAGE_URL)
            self.verify_page_loaded()

    def verify_page_loaded(self):
        """Verify home page is loaded"""
        self.verify_element_present(HomePageLocators.NAV_MENU)
        log_info("Home page loaded successfully")

    # Navigation Methods
    @allure.step("Verify navigation menu is visible")
    def verify_navigation_menu_visible(self):
        """Verify navigation menu is visible"""
        self.verify_element_visible(HomePageLocators.NAV_MENU)
        return self

    @allure.step("Verify navigation items exist")
    def verify_navigation_items_exist(self):
        """Verify all navigation items exist"""
        nav_items = [
            HomePageLocators.NAV_DASHBOARD ,
            HomePageLocators.NAV_MARKETS,
            HomePageLocators.NAV_TRADING_LINK,
            HomePageLocators.NAV_FEATURES_LINK,
            HomePageLocators.NAV_ABOUT_LINK,
            HomePageLocators.NAV_SUPPORT_LINK
        ]
        for item in nav_items:
            self.verify_element_present(item)
        log_info("All navigation items verified")
        return self

    @allure.step("Click Trading navigation link")
    def click_trading_link(self):
        """Click Trading link"""
        self.click_element(HomePageLocators.NAV_TRADING_LINK)
        log_info("Clicked Trading navigation link")
        return self

    @allure.step("Click Markets navigation link")
    def click_markets_link(self):
        """Click Markets link"""
        self.click_element(HomePageLocators.NAV_MARKETS)
        log_info("Clicked Markets navigation link")
        return self

    @allure.step("Click About navigation link")
    def click_about_link(self,option):
        """Click About link"""
        self.click_element(HomePageLocators.NAV_ABOUT_LINK)
        log_info("Clicked About navigation link")
        if option == "Awards":
            self.click_element(HomePageLocators.NAV_AWARDS)
        if option == "WhyMultiBank":
            self.click_element(HomePageLocators.NAV_WHYMULTIBANK)

        log_info("Clicked Awards option navigation link")
        return self

    @allure.step("Click Support navigation link")
    def click_support_link(self):
        """Click Support link (replaces old contact method)"""
        self.click_element(HomePageLocators.NAV_SUPPORT_LINK)
        log_info("Clicked Support navigation link")
        return self

    # Trading Section Methods
    @allure.step("Verify trading section is visible")
    def verify_trading_section_visible(self):
        """Verify trading section is visible"""
        self.verify_element_visible(HomePageLocators.TRADING_SECTION)
        return self

    @allure.step("Get trading pairs count")
    def get_trading_pairs_count(self):
        """Get count of trading pairs"""
        count = self.get_elements_count(HomePageLocators.TRADING_PAIRS)
        log_info(f"Trading pairs count: {count}")
        return count

    @allure.step("Verify trading pairs are displayed")
    def verify_trading_pairs_displayed(self):
        """Verify trading pairs are displayed"""
        assert self.get_trading_pairs_count() > 0, "No trading pairs found"
        log_info("Trading pairs are displayed")
        return self

    @allure.step("Verify trading pair structure")
    def verify_trading_pair_structure(self):
        """Verify trading pair has correct structure"""
        pairs = self.get_elements(HomePageLocators.TRADING_PAIRS)

        for pair in pairs[:3]:  # Check first 3 pairs
            # Verify pair has name
            pair_name = pair.find_element(*HomePageLocators.TRADING_PAIR_NAME)
            assert pair_name.text, "Pair name is empty"

            # Verify pair has price
            pair_price = pair.find_element(*HomePageLocators.TRADING_PAIR_PRICE)
            assert pair_price.text, "Pair price is empty"

            # Verify pair has change percentage
            pair_change = pair.find_element(*HomePageLocators.TRADING_PAIR_CHANGE)
            assert pair_change.text, "Pair change is empty"

        log_info("Trading pair structure verified")
        return self

    @allure.step("Verify category filters exist")
    def verify_category_filters_exist(self):
        """Verify category filters exist"""
        filters_count = self.get_elements_count(HomePageLocators.CATEGORY_FILTERS)
        assert filters_count > 0, "No category filters found"
        log_info(f"Category filters count: {filters_count}")
        return self

    # Marketing Banner Methods
    @allure.step("Verify marketing banners appear at bottom")
    def verify_marketing_banners_visible(self):
        """Verify marketing banners are visible"""
        self.scroll_to_bottom()
        self.verify_element_visible(HomePageLocators.MARKETING_BANNER)
        log_info("Marketing banners are visible at bottom")
        return self

    @allure.step("Get marketing banners count")
    def get_marketing_banners_count(self):
        """Get count of marketing banners"""
        count = self.get_elements_count(HomePageLocators.MARKETING_BANNER)
        return count

    # Download Section Methods
    @allure.step("Verify download section is visible")
    def verify_download_section_visible(self):
        """Verify download section is visible"""
        self.scroll_to_element(HomePageLocators.DOWNLOAD_SECTION)
        self.verify_element_visible(HomePageLocators.DOWNLOAD_SECTION)
        return self

    @allure.step("Verify App Store link exists")
    def verify_app_store_link_exists(self):
        """Verify App Store link exists"""
        self.verify_element_present(HomePageLocators.APP_STORE_LINK)
        log_info("App Store link exists")
        return self

    @allure.step("Verify Google Play link exists")
    def verify_google_play_link_exists(self):
        """Verify Google Play link exists"""
        self.verify_element_present(HomePageLocators.GOOGLE_PLAY_LINK)
        log_info("Google Play link exists")
        return self

    @allure.step("Click App Store link")
    def click_app_store_link(self):
        """Click App Store link"""
        original_window = self.driver.current_window_handle
        self.click_element(HomePageLocators.APP_STORE_LINK)
        log_info("Clicked App Store link")
        return original_window

    @allure.step("Click Google Play link")
    def click_google_play_link(self):
        """Click Google Play link"""
        original_window = self.driver.current_window_handle
        self.click_element(HomePageLocators.GOOGLE_PLAY_LINK)
        log_info("Clicked Google Play link")
        return original_window

    # General Methods
    @allure.step("Verify footer exists")
    def verify_footer_exists(self):
        """Verify footer exists"""
        self.scroll_to_bottom()
        self.verify_element_present(HomePageLocators.FOOTER)
        return self

    @allure.step("Get page title")
    def get_home_page_title(self):
        """Get home page title"""
        return self.get_page_title()