import allure
import os


def attach_screenshot(page, name: str = "screenshot", save_dir: str = "tests/login/screenshot"):
    filename = f"{name}.png"
    file_path = os.path.join(save_dir, filename)
    screenshot = page.screenshot(path=file_path)
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
