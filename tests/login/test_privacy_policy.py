import pytest
import allure

from config import BASE_URL
from helpers.allure_screenshot_function import attach_screenshot


@pytest.mark.test_login_page
@pytest.mark.regression_login
@allure.feature('Privacy Policy')
@allure.story('Correct page Privacy Policy')
def test_privacy_policy(page):
    page.goto(BASE_URL)
    with allure.step(''):
        page.get_by_role("link", name="Privacy Policy").click()
    with allure.step(''):
        assert page.get_by_text('Privacy Policy Generator')
    attach_screenshot(page, 'privacy policy')

    # page.screenshot(path="tests/login/screenshot/privacy_policy.png")
