import pytest
import allure

from config import BASE_URL
from helpers.allure_screenshot_function import attach_screenshot


@pytest.mark.test_login_page
@allure.feature('Validation personalId field')
@allure.story('correct tooltip under the personal id field')
def test_displaying_the_correct_tooltip_under_the_personal_id_field(page):
    page.goto(BASE_URL)
    with allure.step('Enter incorrect id in the personal id field'):
        page.get_by_role("textbox", name="Personal ID").fill("000005")
    with allure.step('press the Tab button'):
        page.get_by_role("textbox", name="Personal ID").press("Tab")
    with allure.step('The correct tooltip text is displayed below the field'):
        assert page.get_by_text("Fill in your identification")
        attach_screenshot(page, 'validation_id_field')

    # page.screenshot(path="tests/login/screenshot/validation_id_field.png")
