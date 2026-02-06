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

def test_error_with_login_with_empty_credentials(page):
    login_page = LoginPage(page)
    login_page.login("", "")
    error_username = page.get_by_text("Required").first
    error_password = page.get_by_text("Required").nth(1)
    expect(error_username).to_have_text("Required")
    expect(error_password).to_have_text("Required")

def test_err_with_login_with_empty_pass(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "")
    error_password = page.get_by_text("Required")
    expect(error_password).to_have_text("Required")

def test_error_with_login_with_empty_username(page):
    login_page = LoginPage(page)
    login_page.login("","admin123")
    error_uname = page.get_by_text("Required")
    expect(error_uname).to_have_text("Required")
