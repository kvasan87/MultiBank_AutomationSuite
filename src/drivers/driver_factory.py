import os
import sys
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    """Factory for creating WebDriver instances"""

    @staticmethod
    def create_driver(browser="chrome", headless=False, remote_url=None):
        """
        Create and return WebDriver instance

        Args:
            browser: Browser type (chrome, firefox, edge)
            headless: Run in headless mode
            remote_url: Remote WebDriver URL for grid execution

        Returns:
            WebDriver instance
        """
        print(f"Creating {browser} WebDriver instance (headless={headless})")

        if remote_url:
            return DriverFactory._create_remote_driver(browser, remote_url)

        browser_lower = browser.lower() if browser else "chrome"

        if browser_lower == "chrome":
            return DriverFactory._create_chrome_driver(headless)
        elif browser_lower == "firefox":
            return DriverFactory._create_firefox_driver(headless)
        elif browser_lower == "edge":
            return DriverFactory._create_edge_driver(headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _get_chrome_driver_path():
        """Get ChromeDriver executable path with robust validation (Windows-safe)."""
        try:
            driver_path = ChromeDriverManager().install()
            if driver_path and os.path.isfile(driver_path):
                lower = driver_path.lower()
                # If webdriver-manager returned a chromedriver exe -> good
                if lower.endswith("chromedriver.exe") or lower.endswith("chromedriver"):
                    return driver_path
                # If it mistakenly returned the Chrome browser, try to locate chromedriver nearby
                if lower.endswith("chrome.exe"):
                    candidate_dir = os.path.dirname(driver_path)
                    # check same directory
                    for f in os.listdir(candidate_dir):
                        if f.lower().startswith("chromedriver") and f.lower().endswith(".exe"):
                            return os.path.join(candidate_dir, f)
                    # walk parent directories looking for chromedriver.exe
                    parent = os.path.dirname(candidate_dir)
                    for root, _, files in os.walk(parent):
                        for f in files:
                            if f.lower().startswith("chromedriver") and f.lower().endswith(".exe"):
                                return os.path.join(root, f)
                # otherwise return if it looks executable
                return driver_path
        except Exception as e:
            print(f"WebDriver-Manager error: {e}")

        # Try system PATH
        for name in ("chromedriver.exe", "chromedriver"):
            chrome_path = shutil.which(name)
            if chrome_path and os.path.isfile(chrome_path):
                return chrome_path

        # Check webdriver-manager cache
        wdm_cache = os.path.join(os.path.expanduser("~"), ".wdm", "drivers", "chromedriver")
        if os.path.isdir(wdm_cache):
            for root, _, files in os.walk(wdm_cache):
                for f in files:
                    if f.lower().startswith("chromedriver") and f.lower().endswith(".exe"):
                        return os.path.join(root, f)

        # Common fallback locations (Windows)
        if sys.platform == "win32":
            common_dirs = [
                r"C:\chromedriver",
                r"C:\Program Files\chromedriver",
                r"C:\Program Files (x86)\chromedriver",
                r"C:\Windows\System32",
            ]
            for d in common_dirs:
                p = os.path.join(d, "chromedriver.exe")
                if os.path.isfile(p):
                    return p

        return None

    @staticmethod
    def _create_chrome_driver(headless=False):
        """Create Chrome WebDriver with better error handling"""
        try:
            options = ChromeOptions()

            # Basic options
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            # Stability options
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            # Performance options
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-plugins")
            options.add_argument("--disable-popup-blocking")

            if headless:
                options.add_argument("--headless=new")

            # Set download directory
            download_dir = os.path.join(os.getcwd(), "downloads")
            os.makedirs(download_dir, exist_ok=True)
            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option("prefs", prefs)

            # Get driver path
            driver_path = DriverFactory._get_chrome_driver_path()

            # Guard: if a browser binary was returned accidentally, ignore it
            if driver_path and driver_path.lower().endswith("chrome.exe"):
                print(f"Warning: found browser binary at {driver_path}, not a chromedriver executable. Ignoring.")
                driver_path = None

            if driver_path:
                print(f"Using ChromeDriver: {driver_path}")
                service = ChromeService(driver_path)
            else:
                print("ChromeDriver not found, attempting without explicit path (webdriver will try default).")
                service = ChromeService()

            driver = webdriver.Chrome(service=service, options=options)
            driver.implicitly_wait(5)

            print("✓ Chrome WebDriver created successfully")
            return driver

        except Exception as e:
            print(f"✗ Failed to create Chrome WebDriver: {str(e)}")
            print("\nTroubleshooting:")
            print("1. Install Chrome browser: https://www.google.com/chrome/")
            print("2. ChromeDriver downloads: https://chromedriver.chromium.org/downloads")
            print("3. Run: pip install --upgrade webdriver-manager (https://pypi.org/project/webdriver-manager/)")
            print("4. Clear cache: remove `~/.wdm/` if needed")
            raise

    @staticmethod
    def _create_firefox_driver(headless=False):
        """Create Firefox WebDriver"""
        try:
            options = FirefoxOptions()

            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            if headless:
                options.add_argument("--headless")

            # Set download directory
            download_dir = os.path.join(os.getcwd(), "downloads")
            os.makedirs(download_dir, exist_ok=True)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", download_dir)

            try:
                driver_path = GeckoDriverManager().install()
                service = FirefoxService(driver_path)
            except Exception:
                service = FirefoxService()

            driver = webdriver.Firefox(service=service, options=options)
            driver.implicitly_wait(5)

            print("✓ Firefox WebDriver created successfully")
            return driver

        except Exception as e:
            print(f"✗ Failed to create Firefox WebDriver: {str(e)}")
            raise

    @staticmethod
    def _create_edge_driver(headless=False):
        """Create Edge WebDriver"""
        try:
            options = EdgeOptions()

            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            if headless:
                options.add_argument("--headless=new")

            # Set download directory
            download_dir = os.path.join(os.getcwd(), "downloads")
            os.makedirs(download_dir, exist_ok=True)
            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option("prefs", prefs)

            try:
                driver_path = EdgeChromiumDriverManager().install()
                service = EdgeService(driver_path)
            except Exception:
                service = EdgeService()

            driver = webdriver.Edge(service=service, options=options)
            driver.implicitly_wait(5)

            print("✓ Edge WebDriver created successfully")
            return driver

        except Exception as e:
            print(f"✗ Failed to create Edge WebDriver: {str(e)}")
            raise

    @staticmethod
    def _create_remote_driver(browser, remote_url):
        """Create Remote WebDriver for Grid"""
        try:
            capabilities = {
                "browserName": browser.lower(),
                "browserVersion": "latest",
                "platformName": "linux"
            }

            driver = webdriver.Remote(
                command_executor=remote_url,
                desired_capabilities=capabilities
            )

            driver.implicitly_wait(5)
            print(f"✓ Remote WebDriver created: {remote_url}")
            return driver

        except Exception as e:
            print(f"✗ Failed to create Remote WebDriver: {str(e)}")
            raise

    @staticmethod
    def quit_driver(driver):
        """Quit WebDriver safely"""
        try:
            if driver:
                driver.quit()
                print("✓ WebDriver closed successfully")
        except Exception as e:
            print(f"⚠ Error closing WebDriver: {str(e)}")