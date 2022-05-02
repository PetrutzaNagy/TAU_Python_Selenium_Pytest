from pages.add_remove_elements_page import AddRemoveElementsPage
from assertpy import assert_that, soft_assertions


def test_check_add_remove_elements_page(browser):
    add_page = AddRemoveElementsPage(browser)
    add_page.loadPage()
    with soft_assertions():
        assert_that(add_page.getTitlePage()).is_equal_to("Add/Remove Elements")
        assert_that((add_page.isAddButtonDisplayed()))

def test_add_page(browser):
    add_page = AddRemoveElementsPage(browser)
    add_page.loadPage()
    add_page.clickAddButton()
    assert_that(add_page.getNumberOfDeleteButton()).is_equal_to(1)
    add_page.clickDeleteButton()
    assert_that(add_page.getNumberOfDeleteButton()).is_equal_to(0)


def test_remove_functionality(browser):
    add_page = AddRemoveElementsPage(browser)
    add_page.loadPage()
    for i in range(10):
        add_page.clickAddButton()
        assert_that(add_page.getNumberOfDeleteButton()).is_equal_to(i)
    for i in range(10):
        add_page.clickFirstDeleteButton()
        assert_that(add_page.getNumberOfDeleteButton()).is_equal_to(10 - i)
