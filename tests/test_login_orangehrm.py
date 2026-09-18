import re
from playwright.sync_api import Page

from pages.orange_hrm_login_page import LoginPage
from pages.orange_hrm_home_page import HomePage


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(page=page)
    home_page = HomePage(page=page)

    login_page.login(username="Admin", password="admin123")
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
