from playwright.sync_api import expect
from orangehrm_tests.pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def login(self, username: str, password: str):
        self.goto(self.URL)
        self.page.fill("input[placeholder='Username']", username)
        self.page.fill("input[placeholder='Password']", password)
        self.page.click("button[type='submit']")


