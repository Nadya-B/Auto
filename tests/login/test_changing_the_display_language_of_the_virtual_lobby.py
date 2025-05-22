import allure

from config import BASE_URL
from helpers.allure_screenshot_function import attach_screenshot


@allure.feature('Change language')
def test_changing_the_display_language_of_the_virtual_lobby(page):
    page.goto(BASE_URL)
    with allure.step('Find dropdown menu of languages'):
        combobox = page.get_by_role("combobox")

    with allure.step('Click on dropdown menu of languages'):
        combobox.click()

    with allure.step('Select language He and click on it'):
        he = page.get_by_role("option", name="He")
        he.click()

    with allure.step('Virtual Lobby is displayed in the correct language'):
        assert page.get_by_role("heading", name="שלום")
    attach_screenshot(page, 'Correct language')
