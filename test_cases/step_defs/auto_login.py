from selenium.webdriver.common.by import By

def login_on_web(driver):

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys("test")

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("Test-aplication1")

    driver.find_element(By.ID, "login-button").click()

def log_off(driver):

    driver.get("http://127.0.0.1:3000/")
    driver.find_element(By.CLASS_NAME, "logout").click()