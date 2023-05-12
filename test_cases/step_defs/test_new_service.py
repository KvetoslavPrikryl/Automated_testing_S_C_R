from pytest_bdd import given, when, then, scenarios
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from auto_login import *

scenarios("../features/new_service.feature")

@pytest.fixture
def setup():
    
    global driver 
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    yield driver


@pytest.fixture
@given("I am logged in", target_fixture="I_am_on_login")
def login_admin(setup):

    driver = setup
    driver.get("http://127.0.0.1:3000/prihlasit")

    login_on_web(driver)

@when("I click on button Hlavní stránka")
def click_on_button():

    driver.find_element(By.ID, "main_page").click()

@when("I click on přidat službu button")
def click_on_add_dog_button():

    driver.find_element(By.ID, "add_service").click()

@when("I fill in form")
def fill_in_form():

    driver.find_element(By.ID, "name_new_service").send_keys("Test_service")
    driver.find_element(By.ID, "price_new_service").send_keys(100)

@when("I click on save button")
def save_new_service():

    driver.find_element(By.ID, "save_service_button").click()

@when("I see new service")
def new_service():

    text_new_service = driver.find_element(By.CLASS_NAME, "service_name").text

    if text_new_service == "Test_service":
        print("Nová služba byla úspěšně přidaná.")
        assert True
    else:
        print("Nová služba se nepřidala. Chyba uložení.")
        assert False

@when("I see price")
def price():

    new_price = driver.find_element(By.CLASS_NAME, "price").text

    if new_price == "100 Kč":
        print("Částka k nové službě sedí.")
        assert True
    else: 
        print("Částka k nové službě nesedí. Chyba načtení z databáze.")
        assert False

@when("I delete new service")
def delete_service():

    driver.find_element(By.CLASS_NAME, "delete-servis").click()

    try:
        text_new_service = driver.find_element(By.CLASS_NAME, "service_name").text
        if text_new_service:
            print("Služba nebyla úspěšně vymazána.")
            assert False
    except:
        print("Služba byla úspěšně vymazána.")
        assert True

@then("Log off")
def log_off_admin():

    log_off(driver)

    driver.quit()