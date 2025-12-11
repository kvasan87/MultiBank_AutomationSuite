from enum import Enum
from selenium.webdriver.common.by import By


class HomePageLocators:
    """Locators for Home Page"""

    # Navigation Menu
    NAV_MENU = (By.XPATH, "//div[contains(@class,'style_menu-container')]")
    NAV_DASHBOARD = (By.LINK_TEXT, "Dashboard")
    NAV_MARKETS = (By.LINK_TEXT, "Markets")
    NAV_TRADING_LINK = (By.XPATH, "//*[@id='trade-header-option-open-button']")
    NAV_FEATURES_LINK = (By.XPATH, "//*[@id='features-header-option-open-button']")
    NAV_ABOUT_LINK = (By.XPATH, "//*[@id='about-header-option-open-button']")
    NAV_AWARDS = (By.XPATH, "//div[contains(text(),'Awards')]")
    NAV_WHYMULTIBANK = (By.XPATH, "//div[contains(text(),'Multibank?')]")
    NAV_SUPPORT_LINK = (By.XPATH, "//*[@id='support-header-option-open-button']")

    # Trading Section
    TRADING_SECTION = (By.ID, "trading-section")
    TRADING_PAIRS = (By.CLASS_NAME, "trading-pair")
    TRADING_PAIR_NAME = (By.CLASS_NAME, "pair-name")
    TRADING_PAIR_PRICE = (By.CLASS_NAME, "pair-price")
    TRADING_PAIR_CHANGE = (By.CLASS_NAME, "pair-change")
    CATEGORY_FILTERS = (By.CLASS_NAME, "category-filter")

    # Marketing Banners
    MARKETING_BANNER = (By.CSS_SELECTOR, ".slick-slide.slick-current img.style_image__kiucM")#(By.XPATH, "//img[contains(@class,'style_image__kiucM')]")
    BANNER_CONTAINER = (By.ID, "banner-container")

    # Download Section
    DOWNLOAD_SECTION = (By.XPATH, "//div[contains(@class,'style_app-download-container')]")
    APP_STORE_LINK = (By.XPATH, "//a[contains(@href,'apps.apple')]")
    GOOGLE_PLAY_LINK = (By.XPATH, "//a[contains(@href,'play.google')]")
    DOWNLOAD_BTN = (By.CLASS_NAME, "download-button")

    # Footer
    FOOTER = (By.TAG_NAME, "footer")
    FOOTER_LINKS = (By.XPATH, "//footer//a")


class TradingPageLocators:
    """Locators for Trading Page"""

    SPOT_TRADING_SECTION = (By.ID, "spot-trading")
    TRADING_PAIRS_LIST = (By.CLASS_NAME, "pairs-list")
    PAIR_ITEM = (By.CLASS_NAME, "pair-item")
    PAIR_SYMBOL = (By.CLASS_NAME, "pair-symbol")
    PAIR_VOLUME = (By.CLASS_NAME, "pair-volume")
    PAIR_PRICE_CHART = (By.CLASS_NAME, "price-chart")

    # Category Tabs
    CATEGORY_TAB = (By.CLASS_NAME, "category-tab")
    CRYPTOCURRENCY_TAB = (By.XPATH, "//button[@data-category='crypto']")
    FOREX_TAB = (By.XPATH, "//button[@data-category='forex']")
    METALS_TAB = (By.XPATH, "//button[@data-category='metals']")
    STOCKS_TAB = (By.XPATH, "//button[@data-category='stocks']")


class AboutPageLocators:
    """Locators for About Us Page"""

    ABOUT_HEADER = (By.TAG_NAME, "h1")
    ABOUT_CONTENT = (By.ID, "about-content")
    WHY_MULTILINK_LINK = (By.XPATH, "//a[@href='/why-multilink']")
    COMPANY_DESCRIPTION = (By.CLASS_NAME, "company-description")
    MISSION_STATEMENT = (By.CLASS_NAME, "mission")
    VISION_STATEMENT = (By.CLASS_NAME, "vision")


class WhyMultilinkPageLocators:
    """Locators for Why MultiLink Page"""

    PAGE_HEADER = (By.TAG_NAME, "h1")
    MAIN_CONTENT = (By.ID, "main-content")
    FEATURE_SECTIONS = (By.CLASS_NAME, "feature-section")
    FEATURE_TITLE = (By.CLASS_NAME, "feature-title")
    FEATURE_DESCRIPTION = (By.CLASS_NAME, "feature-description")
    BENEFITS_LIST = (By.CLASS_NAME, "benefits-list")
    BENEFITS_ITEMS = (By.XPATH, "//ul[@class='benefits-list']/li")
    CALL_TO_ACTION = (By.CLASS_NAME, "cta-button")


class CommonLocators:
    """Common Locators Used Across Pages"""

    LOADING_SPINNER = (By.CLASS_NAME, "spinner")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    MODAL_OVERLAY = (By.CLASS_NAME, "modal-overlay")
    PAGE_TITLE = (By.TAG_NAME, "h1")