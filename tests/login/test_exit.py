import pytest
import allure

from config import BASE_URL


@pytest.mark.test_login_page
@allure.feature('Exit button')
@allure.story('click')
def test_exit(page):
    page.goto(BASE_URL)
    with allure.step('Click button Exit'):
        page.get_by_text(' Exit ').click()
    with allure.step('opened page Appointment & Queue'):
        assert page.get_by_text('Appointment & Queue')

        screenshot = page.screenshot(path="tests/login/screenshot/Appointment & Queue.png")
        allure.attach(
            screenshot,
            name='Appointment & Queue',
            attachment_type=allure.attachment_type.PNG
        )
