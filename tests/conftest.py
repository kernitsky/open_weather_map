import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# CREDENTIALS FOR OpenWeatherMap
USER_EMAIL = "some_user_api_test@yopmail.com"
USER_PASSWORD = "1234567890"
FILENAME = 'D:/apikey.txt'


@pytest.fixture()
def webdriver_init():
    return webdriver.Chrome()


@pytest.fixture()
def login_to_open_weather_map(webdriver_init, user_email=USER_EMAIL, user_password=USER_PASSWORD):
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
    yield
    driver.close()


@pytest.fixture()
def save_api_key_to_file(login_to_open_weather_map, webdriver_init, file=FILENAME):
    # getting api-key from user-page

    # if api key doesn't exist - going to web-page and getting it
    if len(open(file, 'r').read()) != 32:
        driver = webdriver_init
        driver.get('https://home.openweathermap.org/api_keys')
        # getting first available api key from the api keys list on 'open weather map'
        apikey = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[1]/pre').text
        driver.close()

        # saving api-key to the file
        f = open(file, 'w')
        f.write(apikey)
        f.close()
    else:
        return open(file, 'r').read()


# this function can take filename as argument but 'by-default' uses 'D:/apikey.txt' as filename.
@pytest.fixture()
def get_api_key_from_file(save_api_key_to_file, file=FILENAME):
    # save_api_key_to_file()
    apikey = open(file, 'r').read()
    return apikey
