from playwright.sync_api import Page


def fill(locator: str, fil_data: str, page: Page):
    page.fill(locator, fil_data)
