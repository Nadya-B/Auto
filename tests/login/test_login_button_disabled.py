import pytest
import allure
from playwright.sync_api import Page

from config import BASE_URL, PERSONAL_ID, BIRTH_DATE
from helpers.fill_function import fill
from tests.login.locators.login_locators import PERSONAL_ID_LOCATOR, BIRTH_DATE_LOCATOR


@pytest.mark.test_login_page
@allure.feature('Log in button disabled')
@pytest.mark.parametrize(
    'scenariy, locator, value',
    [
        ('login button is disabled', None, None),
        ('enter only personal id and check login button is disabled', PERSONAL_ID_LOCATOR, PERSONAL_ID),
        ('enter only birth day and check login button is disabled', BIRTH_DATE_LOCATOR, BIRTH_DATE),
        ('click checkbox terms & conditions', None, None)
    ]
)
def test_login_button_disabled(page: Page, scenariy: str, locator: str, value: str):
    page.goto(BASE_URL)
    if scenariy == 'login button is disabled' or scenariy == 'click checkbox terms & conditions':
        if scenariy == 'click checkbox terms & conditions':
            page.locator('#termsAgreed').click()
        login_button = page.get_by_text('Log in')
        assert login_button.is_disabled()
    else:
        fill(locator=locator, fil_data=value, page=page)
        login_button = page.get_by_text('Log in')
        assert login_button.is_disabled()

    # assert expect(login_button).to_be_disabled()
    # login_button = page.locator('button:has-text("Exit")')
    # expect(login_button).to_be_enabled()
