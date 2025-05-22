import pytest
import allure

from config import BASE_URL
from helpers.allure_screenshot_function import attach_screenshot


@pytest.mark.test_login_page
@allure.feature('Validation birthday field')
@allure.story('Correct tooltip')
def test_check_correct_tooltip_under_birth_date_field(page):
    page.goto(BASE_URL)
    with allure.step('In the year of birth field, enter a year consisting of three digits'):
        page.get_by_role("textbox", name="Birth Year").fill("111")
    with allure.step('Press the Tab button'):
        page.get_by_role("textbox", name="Birth Year").press("Tab")
    with allure.step('The correct tooltip text is displayed below the field'):
        assert page.get_by_text("Fill in your year of birth in 4 digits")
    attach_screenshot(page, 'tooltip under birth day field')

    # page.screenshot(path="tests/login/screenshot/validation_bd_field.png")
