import pytest
from selenium import webdriver

driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from datetime import datetime



# Function to generate unique email addresses
def generate_unique_email():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return "testuser" + timestamp + "@example.com"


"""
---------------------------------------------------
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
---------------------------------------------------
datetime.now(): This calls the now() method from the datetime module, which returns the current local date and time.
.strftime('%Y%m%d%H%M%S'): This method formats the datetime object into a string according to the specified format:
%Y: Year with century as a decimal number (e.g., 2024)
%m: Month as a zero-padded decimal number (e.g., 07 for July)
%d: Day of the month as a zero-padded decimal number (e.g., 27)
%H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 14 for 2 PM)
%M: Minute as a zero-padded decimal number (e.g., 30)
%S: Second as a zero-padded decimal number (e.g., 05)
The resulting timestamp will be a string like "20240727143005"
--------------------------------------------------------------
return "testuser" + timestamp + "@example.com"
--------------------------------------------------------------
This line concatenates three strings:
"testuser": A static string prefix for the email.
timestamp: The dynamically generated timestamp string.
"@example.com": A static string suffix for the email domain.
The resulting string will be something like "testuser20240727143005@example.com"
----------------------------------------------------------------
Summary:
The generate_unique_email() function generates a unique email address each time it is called.
This is done by creating a string with a static prefix ("testuser"), appending the current date and time as a timestamp,
and then appending a static domain suffix ("@example.com"). This ensures that each email generated is unique based on the
exact moment it was created.
"""


@pytest.fixture()
def setup_and_teardown():
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()


def test_registration(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "caret").click()

    register = driver.find_element(By.XPATH, "//a[text()='Register']")
    register.click()

    # Fill in the registration form with unique email
    first_name = driver.find_element(By.ID, 'input-firstname')
    first_name.send_keys('Mohit')

    last_name = driver.find_element(By.ID, 'input-lastname')
    last_name.send_keys('kumar')

    email = driver.find_element(By.ID, 'input-email')
    unique_email = generate_unique_email()
    email.send_keys(unique_email)

    telephone = driver.find_element(By.ID, 'input-telephone')
    telephone.send_keys('1234567890')

    password = driver.find_element(By.ID, 'input-password')
    password.send_keys('securepassword')

    confirm_password = driver.find_element(By.ID, 'input-confirm')
    confirm_password.send_keys('securepassword')

    # Agree to the privacy policy
    privacy_policy = driver.find_element(By.XPATH, "//input[@name='agree']")
    privacy_policy.click()

    # Submit the registration form
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()


def test_regester_with_already_registered_data(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "caret").click()

    register = driver.find_element(By.XPATH, "//a[text()='Register']")
    register.click()

    # Fill in the registration form with unique email
    first_name = driver.find_element(By.ID, 'input-firstname')
    first_name.send_keys('Rohan')

    last_name = driver.find_element(By.ID, 'input-lastname')
    last_name.send_keys('kumar')

    driver.find_element(By.ID, 'input-email').send_keys("rohan@123.com")

    driver.find_element(By.ID, 'input-telephone').send_keys('123456789')

    driver.find_element(By.ID, 'input-password').send_keys('Rohan@123')

    driver.find_element(By.ID, 'input-confirm').send_keys('Rohan@123')

    # Agree to the privacy policy
    privacy_policy = driver.find_element(By.XPATH, "//input[@name='agree']")
    privacy_policy.click()

    # Submit the registration form
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()

    expected_output = "Warning: E-Mail Address is already registered!"
    assert driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
        expected_output)



