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

def test_failed_access_to_protected_url_for_logged_in(page):
    login_page = LoginPage(page)
    login_page.verify_failed_access_to_protected_url()
    expect(page).to_have_url(re.compile("login"))
    expect(page.locator(".oxd-text.oxd-text--h5.orangehrm-login-title")).to_have_text(re.compile("Login"))


def test_user_remains_logged_in_after_page_refresh(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    expect(page).to_have_url(re.compile("dashboard"))
    expect(page.locator("h6")).to_have_text("Dashboard")
    user = page.locator(".oxd-userdropdown-name").text_content()
    page.reload()
    expect(page).to_have_url(re.compile("dashboard"))
    expect(page.locator("h6")).to_have_text("Dashboard")
    user_after_reload = page.locator(".oxd-userdropdown-name").text_content()
    assert user == user_after_reload


def test_protected_pages_are_unavailable_after_logout(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    login_page.logout()
    login_page.verify_failed_access_to_protected_url()
    expect(page).to_have_url(re.compile("login"))
    expect(page.locator(".oxd-text.oxd-text--h5.orangehrm-login-title")).to_have_text(re.compile("Login"))
