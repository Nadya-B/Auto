import pytest
import allure

from config import BASE_URL
from helpers.allure_screenshot_function import attach_screenshot


@pytest.mark.test_login_page
@pytest.mark.regression_login
@allure.feature('Terms & Conditions')
@allure.story('Correct page Terms & Conditions')
def test_terms_conditions(page):
    page.goto(BASE_URL)
    with allure.step('find the Terms & Conditions link and follow it'):
        page.get_by_text(' Terms & Conditions ').click()
    with allure.step('a page with a description of the Terms & Conditions opens'):
        assert page.get_by_text('Terms and Conditions Sample Generator')
    attach_screenshot(page, 'terms_conditions')
    # page.screenshot(path="tests/login/screenshot/Terms and Conditions.png")
