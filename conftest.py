"""
Pytest configuration with custom --browser option
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import logging
from datetime import datetime
import os


# ====================== LOGGING SETUP ======================
def setup_logging():
    """Configure logging for tests"""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"test_{timestamp}.log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


logger = setup_logging()


# ====================== PYTEST HOOKS ======================
def pytest_addoption(parser):
    """Add custom command-line options"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for testing: chrome, firefox, edge. Default: chrome",
        choices=["chrome", "firefox", "edge"]
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--slow",
        action="store",
        default="0",
        type=float,
        help="Slow down browser actions (seconds). Default: 0"
    )


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "smoke: Smoke tests - quick sanity checks"
    )
    config.addinivalue_line(
        "markers", "regression: Regression tests - tests for bug fixes"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests"
    )
    config.addinivalue_line(
        "markers", "navigation: Navigation tests"
    )


# ====================== FIXTURES ======================
@pytest.fixture(scope="session")
def browser_name(request):
    """Get browser name from command-line option"""
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless(request):
    """Get headless mode from command-line option"""
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def slow_mode(request):
    """Get slow mode value from command-line option"""
    return request.config.getoption("--slow")


@pytest.fixture
def driver(browser_name, headless, slow_mode):
    """
    Selenium WebDriver fixture

    Args:
        browser_name: Browser to use (chrome, firefox, edge)
        headless: Run in headless mode
        slow_mode: Delay between actions (seconds)

    Yields:
        WebDriver: Configured Selenium WebDriver instance
    """

    logger.info(f"Starting {browser_name} browser")
    logger.info(f"Headless mode: {headless}")
    logger.info(f"Slow mode: {slow_mode}s")

    # Chrome Configuration
    if browser_name.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()

        # Headless mode
        if headless:
            chrome_options.add_argument("--headless")

        # Common options
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # Set user agent
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36")
        chrome_options.add_argument(f"user-agent={user_agent}")

        # Initialize driver with ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=service, options=chrome_options)

    # Firefox Configuration
    elif browser_name.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        driver_instance = webdriver.Firefox(options=firefox_options)

    # Edge Configuration
    elif browser_name.lower() == "edge":
        edge_options = webdriver.EdgeOptions()
        if headless:
            edge_options.add_argument("--headless")
        driver_instance = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Set implicit wait
    driver_instance.implicitly_wait(10)
    driver_instance.set_page_load_timeout(30)

    # Set slow mode if specified
    if slow_mode > 0:
        logger.info(f"Enabling slow mode: {slow_mode}s delay")
        driver_instance.set_script_timeout(slow_mode * 2)

    logger.info(f"{browser_name.capitalize()} driver initialized successfully")

    yield driver_instance

    # Cleanup
    logger.info(f"Closing {browser_name} browser")
    driver_instance.quit()
    logger.info(f"{browser_name.capitalize()} driver closed")


@pytest.fixture
def wait(driver):
    """
    WebDriverWait fixture for explicit waits

    Yields:
        WebDriverWait: Configured wait object with 10s timeout
    """
    return WebDriverWait(driver, 10)


@pytest.fixture(autouse=True)
def test_logger(request):
    """Log test start and end"""
    logger.info(f"\n{'=' * 70}")
    logger.info(f"Starting test: {request.node.name}")
    logger.info(f"{'=' * 70}")

    yield

    logger.info(f"Finished test: {request.node.name}")
    logger.info(f"{'=' * 70}\n")


# ====================== HOOKS FOR SCREENSHOTS ======================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and call.when == "call":
        if hasattr(item, "funcargs") and "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(screenshot_dir, f"failure_{item.name}_{timestamp}.png")

            try:
                driver.save_screenshot(screenshot_path)
                logger.error(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to save screenshot: {e}")