from pytest_bdd import given, when, then, scenarios
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

scenarios("../features/navbar.feature")

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
    driver.get("http://127.0.0.1:3000/")

    
@when("I see title text")
def find_title_text():

    title_text = driver.find_element(By.ID, "title").text
    
    if title_text == "Vítejte na stránce":
        print("našli jsme nadpis")
        assert True
    
    else: 
        print("Test Failed!")
        assert False

@when("I click on button")
def click_on_button():
    driver.find_element(By.ID, "kennel").click()

@when("I see title text on link")
def verify_ok_login():
    
    title_text = driver.find_element(By.ID, "title").text

    if title_text == "Naši":
        print("Nadpis: Naši")
        assert True
    elif title_text == "Péče o zvířata":
        print("Nadpis: Péče o zvířata")
        assert True
    else: 
        print("Test Failed!")
        assert False

@when("I click on second button")
def click_on_second_button():

    driver.find_element(By.ID, "service").click()

@when("I click third button")
def click_on_third_button():

    driver.find_element(By.ID, "contact").click()

@then("I see the last title text on link")
def the_last_title():

    title_text = driver.find_element(By.ID, "title").text

    if title_text == "Kontakt":
        print("Nadpis: Kontakt")
        assert True
    else: 
        print("Test Failed!")
        assert False

    driver.quit()