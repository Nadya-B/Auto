import pytest
import allure

from config import BASE_URL, PERSONAL_ID, BIRTH_DATE
from helpers.allure_screenshot_function import attach_screenshot
from helpers.fill_function import fill
from tests.login.locators.login_locators import PERSONAL_ID_LOCATOR, BIRTH_DATE_LOCATOR


@pytest.mark.test_login_page
@allure.feature('Field input')
@allure.story('Input fields are filled')
def test_valid_login_input(page):
    page.goto(BASE_URL)
    with allure.step('Fill the personal id field with a valid value'):
        fill(locator=PERSONAL_ID_LOCATOR, fil_data=PERSONAL_ID, page=page)
    with allure.step('Fill the date of birth field with a valid value'):
        fill(locator=BIRTH_DATE_LOCATOR, fil_data=BIRTH_DATE, page=page)
    with allure.step('The personal id field is filled'):
        assert page.locator(PERSONAL_ID_LOCATOR).input_value() == PERSONAL_ID
    with allure.step('Date of birth field is filled in'):
        assert page.locator(BIRTH_DATE_LOCATOR).input_value() == BIRTH_DATE
    attach_screenshot(page, 'login_inputs-filled')

    # page.screenshot(path="tests/login/screenshot/login_inputs-fill.png")
    # второй сбособ получения данных без локаторов
    # fill(BIRTH_DATE_LOCATOR, BIRTH_DATE, page)
