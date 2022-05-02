import pytest

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from assertpy import assert_that, soft_assertions


def test_successful_login(browser):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert_that(secure_page.get_current_url()).ends_with("/secure")
    assert_that(secure_page.get_flash_message()).contains("You logged into a secure area!")


'''example with parametrize test'''
testdata = [
    ("tomsmith", "fvdvv", "Your password is invalid!"),
    ("CXXVX", "SuperSecretPassword!", "Your username is invalid!"),
    ("", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "", "Your password is invalid!"),
    (" ", " ", "Yourpassword is invalid!"),
]


@pytest.mark.parametrize("user,password,message", testdata)
def test_negative_login(browser, user, password, message):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login(user, password)
    assert_that(login_page.get_current_url()).ends_with("/login")
    assert_that(login_page.get_flash_message()).contains(message)


'''example with soft assertions'''


def test_login_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    with soft_assertions():
        assert_that(login_page.get_current_url()).ends_with("/login")
