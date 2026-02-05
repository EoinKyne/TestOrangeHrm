from playwright.sync_api import expect
from orangehrm_tests.pages.login_page import LoginPage
import re


def test_verify_forgotten_password_link(page):
    login_page = LoginPage(page)
    login_page.verify_forgot_password_link()
    expect(page).to_have_url(re.compile("requestPasswordResetCode"))