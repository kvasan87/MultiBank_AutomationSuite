echo "=== MultiBank Test Automation Framework ==="
echo ""

echo "Step 1: Cleaning previous test results..."
rm -rf allure-results
rm -rf reports/
rm -rf screenshots/
rm -rf logs/
mkdir -p allure-results

echo "Step 2: Running test suite..."
pytest tests/ -v --alluredir allure-results --tb=short --color=yes -n 2
allure serve allure-results