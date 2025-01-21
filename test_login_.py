import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


@pytest.fixture()
def setup_and_teardown():
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()


def test_login_with_valid_credential(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "caret").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("rohan@123.com")
    driver.find_element(By.ID, "input-password").send_keys("@123")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    expected_text = "My Account"
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']").text.__eq__(expected_text)


def test_login_without_details(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "caret").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_text = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
        expected_text)
