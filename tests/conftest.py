import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('PFCards/tests/chromedriver.exe')
    pytest.driver.get("http://petfriends.skillfactory.ru/login")

    yield

    pytest.driver.quit()

@pytest.fixture()
def my_pets_profile_page():
    WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located
        ((By.ID, 'email')))

    pytest.driver.find_element(By.ID, 'email').send_keys('bobo@mail.ru')

    WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located
        ((By.ID, 'pass')))

    pytest.driver.find_element(By.ID, 'pass').send_keys('sirius')

    WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located
        ((By.CSS_SELECTOR, "button[type='submit']")))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located
        ((By.LINK_TEXT, 'Мои питомцы')))

    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()


@pytest.fixture()
def wait_table_cards():
    WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located
        ((By.CSS_SELECTOR, '.table.table-hover tbody tr')))


@pytest.fixture()
def wait_profile_cards():
    WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located
        ((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
