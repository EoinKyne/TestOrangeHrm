Playwright tests on OrangeHRM

dependencies:
pip install playwright pytest
pip install playwright
playwright install chromium

Pages:
Base page (shared behavior)
pages/base_page.py

Login page object
pages/login_page.py

Tests:
conftest.py (centralize page creation & teardown)
test_login.py (login tests)
test_forgot_password.py (forgot password tests)
test_socials_links_login_page.py (social links tests)

Runner:
runner.py (run tests with pytest and playwright)