import pytest
import allure

from config import BASE_URL, PERSONAL_ID, BIRTH_DATE
from helpers.fill_function import fill
from tests.login.locators.login_locators import PERSONAL_ID_LOCATOR, BIRTH_DATE_LOCATOR


@pytest.mark.test_login_page
@allure.feature('')
@allure.story('')
def test_login_button_enabled(page):
    page.goto(BASE_URL)
    with allure.step(''):
        fill(locator=PERSONAL_ID_LOCATOR, fil_data=PERSONAL_ID, page=page)
    with allure.step(''):
        fill(locator=BIRTH_DATE_LOCATOR, fil_data=BIRTH_DATE, page=page)
    with allure.step(''):
        page.locator('#termsAgreed').click()
        login_button = page.get_by_text('Log in')
    with allure.step(''):
        assert login_button.is_enabled()
