# MultiBank Trading Platform - Test Automation Framework

## 📋 Overview
**Task 1: Web UI Automation Framework **
A production-grade web automation framework for testing the MultiBank trading platform (https://trade.multibank.io/). Built with **Python**, **Selenium**, and **Pytest**, featuring comprehensive test coverage, Allure reporting, and CI/CD integration.

**Task 2 2: String Character Frequency - Please Refer to Task2/CountChar.py**

## ✨ Key Features

- ✅ **Page Object Model** - Clean, maintainable code structure
- ✅ **Cross-Browser Testing** - Chrome, Firefox, Edge support
- ✅ **Smart Wait Strategies** - Explicit waits with custom conditions
- ✅ **Allure Reporting** - Beautiful, comprehensive test reports
- ✅ **Data-Driven Tests** - External test data management
- ✅ **Parallel Execution** - pytest-xdist for faster testing
- ✅ **CI/CD Ready** - GitHub Actions integration
- ✅ **Automatic Screenshots** - Failure diagnostics
- ✅ **Retry Mechanisms** - Handles flaky tests
- ✅ **Comprehensive Logging** - Debug support

## 🏗️ Project Structure

```
multibank-automation-framework/
├── config/                    # Configuration files
│   ├── config.yaml           # Test configuration
│   └── test_data.json        # Test data
├── src/
│   ├── pages/                # Page Objects
│   │   ├── base_page.py      # Base class
│   │   ├── home_page.py      # Home page
│   │   ├── about_page.py     # About page
│   │   └── why_multilink_page.py  # Why MultiLink page
│   ├── drivers/              # WebDriver management
│   │   └── driver_factory.py # Cross-browser driver factory
│   ├── utils/                # Utilities
│   │   ├── logger.py         # Logging
│   │   ├── wait_helpers.py   # Wait strategies
│   │   └── ...
│   └── constants/            # Constants
│       └── locators.py       # UI locators
├── tests/                    # Test files
│   ├── conftest.py          # Pytest fixtures
│   ├── test_navigation.py   # Navigation tests
│   ├── test_trading_functionality.py  # Trading tests
│   └── test_content_validation.py     # Content tests
├── reports/                  # Test reports
│   └── allure-results/      # Allure results
├── requirements.txt          # Dependencies
├── pytest.ini               # Pytest configuration
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Chrome/Firefox/Edge browser (latest version)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/multibank-automation.git
cd multibank-automation
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Verify installation:**
```bash
pytest --version
allure --version
```

## 🧪 Running Tests

### Basic Execution

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_navigation.py

# Run specific test
pytest tests/test_navigation.py::TestNavigation::test_navigation_menu_visible
```

### By Test Marker

```bash
# Run only smoke tests
pytest tests/ -m smoke

# Run only regression tests
pytest tests/ -m regression

# Run both smoke and regression
pytest tests/ -m "smoke or regression"
```

### Cross-Browser Testing

```bash
# Chrome (default)
pytest tests/ --browser=chrome

# Firefox
pytest tests/ --browser=firefox

# Edge
pytest tests/ --browser=edge

# Headless mode
pytest tests/ --headless
```

### Parallel Execution

```bash
# Run tests in parallel (4 workers)
pytest tests/ -n 4

# Run with auto-detected number of workers
pytest tests/ -n auto
```

### With Allure Reports

```bash
# Generate Allure results
pytest tests/ --alluredir allure-results

# Generate and serve Allure report
allure serve allure-results

# Generate static report
allure generate allure-results -o allure-report --clean
```

### Retry on Failure

```bash
# Retry failed tests up to 3 times
pytest tests/ --reruns 3 --reruns-delay 2
```

### Test with Coverage

```bash
# Run with coverage report
pytest tests/ --cov=src --cov-report=html
```

## 📊 Allure Report Usage

### Generate Report

```bash
# Run tests and collect results
pytest tests/ --alluredir allure-results

# Serve report locally (auto-opens browser)
allure serve allure-results

# Generate static HTML report
allure generate allure-results -o allure-report --clean
```

### Report Includes

- ✅ Test execution overview
- ✅ Feature/Story breakdown
- ✅ Step-by-step test logs
- ✅ Failed test analysis
- ✅ Screenshots on failure
- ✅ Timing statistics
- ✅ Historical trends

## 🔧 Configuration

### Environment Variables

```bash
# Set browser
export BROWSER=chrome

# Enable headless mode
export HEADLESS=true

# Set remote WebDriver URL
export REMOTE_URL=http://localhost:4444
```

### Pytest Configuration

Edit `pytest.ini` to customize:
- Test discovery patterns
- Markers
- Timeouts
- Logging

### Driver Configuration

Edit `src/drivers/driver_factory.py` to:
- Add proxy settings
- Configure cookies
- Set additional options
- Customize timeouts

## 📝 Test Coverage

### Navigation & Layout Tests [Completed]
- Navigation menu visibility
- Navigation items functionality
- Page navigation
- Layout responsiveness

### Content Validation Tests [Completed]
- Marketing banners
- Download links
- About Us page
- Why MultiLink page
- Page component rendering

### Trading Functionality Tests  [Apologies I was not able to Complete]
- Trading section visibility
- Trading pairs display
- Data structure validation
- Category filters

## 🎯 Test Scenarios

### Scenario 1: Complete User Journey
1. Load home page
2. Verify navigation menu
3. View trading pairs
4. Navigate to About page
5. View Why MultiLink page
6. Download app links

### Scenario 2: Trading Data Validation
1. Load home page
2. Verify trading section
3. Validate pair structure
4. Check category filters
5. Verify data updates

### Scenario 3: Content Accuracy
1. Verify all static content
2. Check banners appear
3. Validate links work


## 🔍 Debugging

### Enable Verbose Logging

```bash
pytest tests/ -v --log-cli-level=DEBUG
```

### Take Screenshots

Screenshots are automatically taken on test failure in `screenshots/` directory.

### View Logs

Logs are saved in `logs/` directory with timestamps.

### Run Single Test with Debug

```bash
pytest tests/test_navigation.py::TestNavigation::test_navigation_menu_visible -s -v
```

## 🔄 CI/CD Integration

### GitHub Actions

The framework includes GitHub Actions workflow (`.github/workflows/test_automation.yml`) that:

- Runs on push/PR to main/develop
- Tests on multiple Python versions
- Supports cross-browser testing
- Generates Allure reports
- Publishes reports to GitHub Pages
- Uploads artifacts

### Manual Trigger

```bash
# Push to trigger tests
git push origin feature-branch

# View results in GitHub Actions tab
```

### Local CI Simulation

```bash
# Install Act (local GitHub Actions runner)
# https://github.com/nektos/act

act -j test
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| selenium | 4.15.2 | Web automation |
| pytest | 7.4.3 | Test framework |
| pytest-xdist | 3.5.0 | Parallel execution |
| allure-pytest | 2.13.2 | Reporting |
| webdriver-manager | 4.0.2 | Driver management |
| pyyaml | 6.0.1 | Configuration |

## 🎓 Best Practices

### Test Design
- ✅ Independent tests (no dependencies)
- ✅ Clear test names (describe what's tested)
- ✅ Single responsibility (one assertion focus)
- ✅ Deterministic results (no flakiness)

### Code Quality
- ✅ DRY principle (reusable methods)
- ✅ Page Object Model (separation of concerns)
- ✅ Proper wait strategies (no sleep)
- ✅ Descriptive variable names

### Maintenance
- ✅ Update locators in one place
- ✅ Use external test data
- ✅ Document complex logic
- ✅ Keep base class utilities

## 🐛 Troubleshooting

### WebDriver Issues

```bash
# Update chromedriver
webdriver-manager chrome --download-driver

# Check driver path
python -c "from webdriver_manager.chrome import ChromeDriverManager; print(ChromeDriverManager().install())"
```

### Element Not Found

- Increase wait timeout
- Verify locator is correct
- Check if element is in iframe
- Inspect DOM with browser DevTools

### Timeout Issues

- Increase `DEFAULT_TIMEOUT` in `wait_helpers.py`
- Check network connectivity
- Verify page loads correctly
- Add explicit wait conditions

### Parallel Execution Issues

- Run sequentially first: `pytest tests/`
- Check for shared state
- Ensure proper fixture scopes
- Use unique test data

## 📚 Additional Resources

- [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- [Page Object Model](https://selenium.dev/documentation/test_practices/encouraged/page_object_models/)

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## ✅ Quality Checklist

- [x] Page Object Model implementation
- [x] Cross-browser support
- [x] Smart wait strategies
- [x] Allure reporting
- [x] Parallel execution
- [x] CI/CD integration
- [x] Comprehensive logging
- [x] Error handling
- [x] Screenshot on failure
- [x] Documentation

## 🎉 Success Criteria

All tests should:
1. ✅ Pass consistently (no flakiness)
2. ✅ Execute in under 5 minutes (parallel)
3. ✅ Generate Allure reports
4. ✅ Include clear failure diagnostics
5. ✅ Run on multiple browsers
6. ✅ Support CI/CD integration
7. ✅ Have zero hard-coded values
8. ✅ Follow POM pattern

---

**Last Updated:** December 2024
**Framework Version:** 1.0
**Test Coverage:** 30+ test cases across 4 suites
