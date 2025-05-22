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
        page.wait_for_function(
            """() => document.querySelector('[role="combobox"]')?.getAttribute('aria-expanded') === 'true'"""
        )

    with allure.step('Select language He and click on it'):
        he = page.get_by_role("option", name="He")
        he.wait_for(state="visible")
        he.click()

    with allure.step('Wait until the interface updates to Hebrew'):
        page.get_by_role("heading", name="שלום").wait_for(state="visible")

    with allure.step('Virtual Lobby is displayed in the correct language'):
        heading = page.get_by_role("heading", name="שלום")
        assert heading.is_visible(), "Заголовок 'שלום' не відображається"
    attach_screenshot(page, 'Correct language')