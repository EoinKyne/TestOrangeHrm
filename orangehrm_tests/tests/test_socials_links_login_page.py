from playwright.sync_api import expect
from orangehrm_tests.pages.login_page import LoginPage
import re


def test_verify_linkedin_link(page):
    login_page = LoginPage(page)
    with page.expect_popup() as popup_info:
        login_page.verify_linkedin_link()
    new_page = popup_info.value
    #new_page.wait_for_load_state()
    expect(new_page).to_have_url(re.compile("linkedin") and re.compile("orangehrm"))


def test_verify_facebook_link(page):
    login_page = LoginPage(page)
    with page.expect_popup() as popup_info:
        login_page.verify_facebook_link()
    new_page = popup_info.value
    #new_page.wait_for_load_state()
    expect(new_page).to_have_url(re.compile("facebook") and re.compile("OrangeHRM"))

def test_verify_twitter_link(page):
    login_page = LoginPage(page)
    with page.expect_popup() as popup_info:
        login_page.verify_twitter_link()
    new_page = popup_info.value
    expect(new_page).to_have_url(re.compile("x") and re.compile("orangehrm"))

def test_verify_youtube_link(page):
    login_page = LoginPage(page)
    with page.expect_popup() as popup_info:
        login_page.verify_youtube_link()
    new_page = popup_info.value
    expect(new_page).to_have_url(re.compile("youtube") and re.compile("OrangeHRMInc"))

