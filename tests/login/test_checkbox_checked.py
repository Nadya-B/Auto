import pytest
import allure

from config import BASE_URL
from helpers.allure_screenshot_function import attach_screenshot


@pytest.mark.test_login_page
@pytest.mark.regression_login
@allure.feature('check_box terms and conditions is checked')
@allure.story('checked')
def test_checkbox_checked(page):
    page.goto(BASE_URL)
    with allure.step('checkbox is present on the login page'):
        checkbox = page.get_by_role("checkbox", name="I agree to Terms & Conditions")
    with allure.step('click on the checkbox'):
        checkbox.click()
    with allure.step('checkbox is checked'):
        assert checkbox.is_checked()
        attach_screenshot(page, 'check-box checked')

        # page.screenshot(path="tests/login/screenshot/checkbox.png")
