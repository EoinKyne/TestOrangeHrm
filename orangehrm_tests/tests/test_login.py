from orangehrm_tests.pages.login_page import LoginPage
from playwright.sync_api import expect
import re

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    expect(page).to_have_url(re.compile("dashboard"))
    expect(page.locator("h6")).to_have_text("Dashboard")


def test_unsuccessful_login(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "Admin123")
    error = page.locator(".oxd-alert-content-text")
    expect(error).to_have_text("Invalid credentials")