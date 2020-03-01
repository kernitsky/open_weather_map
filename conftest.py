import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import constants


@pytest.fixture()
def webdriver_init():
    return webdriver.Chrome()


@pytest.fixture()
def login_to_open_weather_map(webdriver_init, user_email=constants.USER_EMAIL, user_password=constants.USER_PASSWORD):
    # webdriver initialization
    driver = webdriver_init
    driver.get("https://openweathermap.org/home/sign_in")

    # enter login
    elem = driver.find_element_by_id("user_email")
    elem.send_keys(user_email)

    # enter password
    elem = driver.find_element_by_id("user_password")
    elem.send_keys(user_password)
    elem.send_keys(Keys.RETURN)
    yield driver
    driver.close()


@pytest.fixture()
def save_api_key_to_file(login_to_open_weather_map):
    # getting api-key from user-page
    driver = login_to_open_weather_map
    driver.get('https://home.openweathermap.org/api_keys')

    # getting first available api key from the api keys list on 'open weather map'
    apikey = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[1]/pre').text

    # saving api-key to the file
    f = open('apikey.txt', 'w')
    f.write(apikey)
    f.close()


@pytest.fixture()
def get_api_key_from_file(save_api_key_to_file):
    file = open('apikey.txt', 'r')
    apikey = file.read()
    file.close()
    return apikey
