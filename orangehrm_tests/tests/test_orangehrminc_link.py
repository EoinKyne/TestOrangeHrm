from playwright.sync_api import expect
from orangehrm_tests.pages.login_page import LoginPage
import re


def test_orangehrminc_link(page):
    login_page = LoginPage(page)
    with page.expect_popup() as popup_info:
        login_page.verify_orangehrminc_link()
    new_page = popup_info.value
    expect(new_page).to_have_url("https://www.orangehrm.com/")