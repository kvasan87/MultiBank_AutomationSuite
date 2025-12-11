from src.pages.base_page import BasePage
from src.constants.locators import AboutPageLocators
from src.utils.logger import log_info
import allure


class AboutPage(BasePage):
    """About Us Page Object"""

    PAGE_URL = "https://trade.multibank.io/about"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Load about page"""
        with allure.step("Navigate to About Page"):
            self.navigate_to_url(self.PAGE_URL)
            self.verify_page_loaded()

    def verify_page_loaded(self):
        """Verify about page is loaded"""
        self.verify_element_present(AboutPageLocators.ABOUT_HEADER)
        log_info("About page loaded successfully")

    @allure.step("Verify about page header")
    def verify_about_header_present(self):
        """Verify about page header is present"""
        self.verify_element_present(AboutPageLocators.ABOUT_HEADER)
        return self

    @allure.step("Verify about content is visible")
    def verify_about_content_visible(self):
        """Verify about content is visible"""
        self.verify_element_visible(AboutPageLocators.ABOUT_CONTENT)
        return self

    @allure.step("Get about page title")
    def get_about_page_title(self):
        """Get about page title"""
        return self.get_element_text(AboutPageLocators.ABOUT_HEADER)

    @allure.step("Click Why MultiLink link")
    def click_why_multilink_link(self):
        """Click Why MultiLink link"""
        self.click_element(AboutPageLocators.WHY_MULTILINK_LINK)
        log_info("Clicked Why MultiLink link")

    @allure.step("Verify Why MultiLink link exists")
    def verify_why_multilink_link_exists(self):
        """Verify Why MultiLink link exists"""
        self.verify_element_present(AboutPageLocators.WHY_MULTILINK_LINK)
        return self

    @allure.step("Verify company description is present")
    def verify_company_description_present(self):
        """Verify company description is present"""
        self.verify_element_present(AboutPageLocators.COMPANY_DESCRIPTION)
        return self

    @allure.step("Verify mission statement is present")
    def verify_mission_statement_present(self):
        """Verify mission statement is present"""
        self.verify_element_present(AboutPageLocators.MISSION_STATEMENT)
        return self

    @allure.step("Verify vision statement is present")
    def verify_vision_statement_present(self):
        """Verify vision statement is present"""
        self.verify_element_present(AboutPageLocators.VISION_STATEMENT)
        return self

    @allure.step("Get company description")
    def get_company_description(self):
        """Get company description text"""
        return self.get_element_text(AboutPageLocators.COMPANY_DESCRIPTION)

    @allure.step("Get mission statement")
    def get_mission_statement(self):
        """Get mission statement text"""
        return self.get_element_text(AboutPageLocators.MISSION_STATEMENT)

    @allure.step("Get vision statement")
    def get_vision_statement(self):
        """Get vision statement text"""
        return self.get_element_text(AboutPageLocators.VISION_STATEMENT)