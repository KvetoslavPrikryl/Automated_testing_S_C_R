from pytest_bdd import given, when, then, scenarios
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auto_login import *

scenarios("../features/login.feature")

@pytest.fixture
def setup():
    
    global driver 
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    yield driver


@pytest.fixture
@given("I am on the link", target_fixture="I_am_on_login")
def I_am_on_link(setup):
    
    driver = setup
    driver.get("http://127.0.0.1:3000/prihlasit")

@when("I see the login web link")
def title_text():

    title_text = driver.find_element(By.ID, "title").text

    if title_text == "Přihlášení":
        assert True

    else:
        print("Nevidím nadpis.")
        assert False

@when("I login on web")
def login_admin():

    login_on_web(driver)

@when("I see welcome title")
def welcome_text():

    welcome_title = driver.find_element(By.ID, "welcome_title").text

    if "Výtej" in welcome_title:
        assert True
    else:
        print("Nepovedlo se přihlásit")
        assert False
    
@then("Log off")
def log_off_admin():

    log_off(driver)

    driver.quit()