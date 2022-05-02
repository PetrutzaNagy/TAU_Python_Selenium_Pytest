from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from assertpy import assert_that


def test_logout(browser):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page.click_logout_button()
    assert_that(login_page.get_current_url()).ends_with("/login")
    assert_that(login_page.get_flash_message()).contains("You logged into a secure area!")
