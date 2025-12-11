from src.pages.base_page import BasePage
from src.constants.locators import WhyMultilinkPageLocators
from src.utils.logger import log_info
import allure


class WhyMultilinkPage(BasePage):
    """Why MultiLink Page Object"""

    PAGE_URL = "https://multibank.io/about/why-multibank"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Load why multilink page"""
        with allure.step("Navigate to Why MultiLink Page"):
            self.navigate_to_url(self.PAGE_URL)
            self.verify_page_loaded()

    def verify_page_loaded(self):
        """Verify page is loaded"""
        self.verify_element_present(WhyMultilinkPageLocators.PAGE_HEADER)
        log_info("Why MultiLink page loaded successfully")

    @allure.step("Verify page header is present")
    def verify_page_header_present(self):
        """Verify page header is present"""
        self.verify_element_present(WhyMultilinkPageLocators.PAGE_HEADER)
        return self

    @allure.step("Verify main content is visible")
    def verify_main_content_visible(self):
        """Verify main content is visible"""
        self.verify_element_visible(WhyMultilinkPageLocators.MAIN_CONTENT)
        return self

    @allure.step("Get page header text")
    def get_page_header_text(self):
        """Get page header text"""
        return self.get_element_text(WhyMultilinkPageLocators.PAGE_HEADER)

    @allure.step("Get feature sections count")
    def get_feature_sections_count(self):
        """Get count of feature sections"""
        count = self.get_elements_count(WhyMultilinkPageLocators.FEATURE_SECTIONS)
        log_info(f"Feature sections count: {count}")
        return count

    @allure.step("Verify feature sections exist")
    def verify_feature_sections_exist(self):
        """Verify feature sections exist"""
        assert self.get_feature_sections_count() > 0, "No feature sections found"
        log_info("Feature sections verified")
        return self

    @allure.step("Verify feature section has title and description")
    def verify_feature_section_structure(self):
        """Verify each feature section has title and description"""
        sections = self.get_elements(WhyMultilinkPageLocators.FEATURE_SECTIONS)

        for section in sections[:3]:  # Check first 3 sections
            title_elements = section.find_elements(*WhyMultilinkPageLocators.FEATURE_TITLE)
            desc_elements = section.find_elements(*WhyMultilinkPageLocators.FEATURE_DESCRIPTION)

            assert len(title_elements) > 0, "Feature section missing title"
            assert len(desc_elements) > 0, "Feature section missing description"

            assert title_elements[0].text, "Feature title is empty"
            assert desc_elements[0].text, "Feature description is empty"

        log_info("Feature section structure verified")
        return self

    @allure.step("Get benefits list items count")
    def get_benefits_list_items_count(self):
        """Get count of benefits list items"""
        count = self.get_elements_count(WhyMultilinkPageLocators.BENEFITS_ITEMS)
        log_info(f"Benefits items count: {count}")
        return count

    @allure.step("Verify benefits list is present")
    def verify_benefits_list_present(self):
        """Verify benefits list is present"""
        self.verify_element_present(WhyMultilinkPageLocators.BENEFITS_LIST)
        return self

    @allure.step("Verify benefits list has items")
    def verify_benefits_list_has_items(self):
        """Verify benefits list contains items"""
        assert self.get_benefits_list_items_count() > 0, "Benefits list is empty"
        log_info("Benefits list has items")
        return self

    @allure.step("Verify all benefits items have text")
    def verify_benefits_items_have_text(self):
        """Verify all benefits items contain text"""
        items = self.get_elements(WhyMultilinkPageLocators.BENEFITS_ITEMS)

        for item in items:
            assert item.text, "Benefit item is empty"

        log_info("All benefits items have text")
        return self

    @allure.step("Verify call-to-action button is present")
    def verify_cta_button_present(self):
        """Verify call-to-action button is present"""
        self.verify_element_present(WhyMultilinkPageLocators.CALL_TO_ACTION)
        return self

    @allure.step("Click call-to-action button")
    def click_cta_button(self):
        """Click call-to-action button"""
        self.click_element(WhyMultilinkPageLocators.CALL_TO_ACTION)
        log_info("Clicked call-to-action button")
        return self

    @allure.step("Scroll through page content")
    def scroll_through_content(self):
        """Scroll through page content"""
        self.scroll_down(500)
        self.scroll_down(500)
        self.scroll_to_bottom()
        log_info("Scrolled through page content")
        return self

    @allure.step("Verify all components render correctly")
    def verify_all_components_render(self):
        """Verify all page components render correctly"""
        self.verify_page_header_present()
        self.verify_main_content_visible()
        self.verify_feature_sections_exist()
        self.verify_benefits_list_present()
        self.verify_cta_button_present()
        log_info("All components verified")
        return self