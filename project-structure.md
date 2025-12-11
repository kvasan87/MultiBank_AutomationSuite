# MultiBank Trading Platform - Test Automation Framework

## Project Structure

```
multibank-automation-framework/
│
├── config/
│   ├── __init__.py
│   ├── config.yaml
│   └── test_data.json
│
├── src/
│   ├── __init__.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   ├── trading_page.py
│   │   ├── about_page.py
│   │   └── why_multilink_page.py
│   │
│   ├── drivers/
│   │   ├── __init__.py
│   │   └── driver_factory.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── config_loader.py
│   │   ├── wait_helpers.py
│   │   ├── screenshot_helper.py
│   │   └── test_data_loader.py
│   │
│   └── constants/
│       ├── __init__.py
│       ├── locators.py
│       ├── messages.py
│       └── urls.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_navigation.py
│   ├── test_trading_functionality.py
│   ├── test_content_validation.py
│   └── test_cross_browser.py
│
├── reports/
│   ├── allure-results/
│   └── allure-report/
│
├── .github/
│   └── workflows/
│       └── test_automation.yml
│
├── requirements.txt
├── pytest.ini
├── conftest.py
├── README.md
└── setup.py
```

## Key Features

- **Page Object Model** - Clean separation of UI interactions and test logic
- **Pytest Framework** - Powerful testing framework with fixtures and parameterization
- **Allure Reporting** - Beautiful, comprehensive test reports
- **Cross-Browser Testing** - Chrome, Firefox, Edge support
- **Data-Driven Tests** - External test data management via JSON
- **Smart Wait Strategies** - Explicit waits with custom conditions
- **Logging & Screenshots** - Automatic failure diagnostics
- **CI/CD Ready** - GitHub Actions integration
- **Retry Mechanisms** - Automatic test retry on flaky failures
- **Parallel Execution** - pytest-xdist for parallel test runs

## Installation & Execution

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ --alluredir allure-results

# Run specific test module
pytest tests/test_navigation.py -v --alluredir allure-results

# Run with cross-browser
pytest tests/ -m "chrome or firefox or edge" --alluredir allure-results

# Generate Allure report
allure serve allure-results

# Run in parallel
pytest tests/ -n 4 --alluredir allure-results
```
