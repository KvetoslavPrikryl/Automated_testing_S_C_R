from pytest_bdd import given, when, then, scenarios
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from auto_login import *

scenarios("../features/add_dog.feature")

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

@when("I click on button Přidat psa")
def click_on_add_dog_button():

    driver.find_element(By.ID, "add_dog").click()

@when("I fill in form")
def fill_in_form():

    driver.find_element(By.ID, "dog_name").clear()
    driver.find_element(By.ID, "dog_name").send_keys("test_dog")

    driver.find_element(By.ID, "dog_link").clear()
    driver.find_element(By.ID, "dog_link").send_keys("test_dog_link")

    driver.find_element(By.ID, "dog_body").clear()
    driver.find_element(By.ID, "dog_body").send_keys("test_dog_body")

    driver.find_element(By.ID, "button_dog_pup").click()
    
@when("I click on button Uložit")
def click_on_save_button():

    driver.find_element(By.ID, "button_save").click()

@when("I click on button Štěňata")
def click_on_pup_button():

    driver.find_element(By.ID, "dog_pup").click()

@when("I see this new dog")
def this_new_dog():

    dog_name = driver.find_element(By.CLASS_NAME, "name_dog").text

    if dog_name == "test_dog":
        print("Byl úspěšně uložen nový pes.")
        assert True
    
    else:
        print("Nebyl nalezen nový pes. Uložení neprobělho v pořádku.")
        assert False

@when("I delete this dog")
def delete_new_dog():

    driver.find_element(By.CLASS_NAME, "delete_dog_button").click()

@when("I dount see this dog")
def no_dog():

    try: 
        dog_name = driver.find_element(By.CLASS_NAME, "name_dog").text
        if dog_name:
            print("Přidaný pes nebyl vymazán.")
            assert False
    except:
        print("Pes byl úspěšně vymazán.")
        assert True

@then("Log off")
def log_off_admin():

    log_off(driver)

    driver.quit()