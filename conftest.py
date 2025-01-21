import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType


@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver

    yield

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Capture screenshots if the test fails
    if rep.when == 'call' and rep.failed:
        driver = getattr(item.cls, 'driver', None)
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    setattr(item, "rep_" + rep.when, rep)
