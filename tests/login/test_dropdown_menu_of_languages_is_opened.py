import pytest
import allure

from config import BASE_URL


@pytest.mark.test_login_page
@allure.feature('Dropdown menu of languages')
@allure.story('dropdown menu of languages is present')
def test_dropdown_menu_for_language_selection_is_opened(page):
    page.goto(BASE_URL)
    with allure.step('Find dropdown menu of languages'):
        combobox = page.get_by_role("combobox")

    with allure.step('Click on dropdown menu of languages'):
        combobox.click()
        page.wait_for_function(
            """() => document.querySelector('[role="combobox"]')?.getAttribute('aria-expanded') === 'true'"""
        )

    with allure.step('Dropdown menu of languages is open'):
        assert combobox.get_attribute("aria-expanded") == "true"

        expect(page.get_by_role("listbox", name="Options list")).to_be_visible()
