def test_search_for_valid_product():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("iphone")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT, "iPhone").is_displayed()
    driver.quit()


def test_search_for_invalid_product():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("laptop")
    driver.find_element(By.XPATH, "//button[@.class='btn btn-default btn-lg']").click()
    expected_output = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_output)
    driver.quit()


def test_search_without_providing_any_product():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    expected_output = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_output)
    driver.quit()
