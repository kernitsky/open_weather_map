import allure
import requests

# city ID constant for OpenWeather API. By default - Ukraine, Odessa, 65000
# List of CityID's can be found here http://bulk.openweathermap.org/sample/city.list.json.gz
CITY_ID = '698740'  # Ukraine, Odessa, 65000
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
EXPECTED_WEATHER = 'sunny'


@allure.feature('status200_check')
@allure.story('open_weather_map')
def test_owp_status(get_api_key_from_file):
    params = {'id': str(CITY_ID), 'appid': get_api_key_from_file}
    response = requests.get(BASE_URL, params)
    assert response.status_code == 200


@allure.feature('weather_check')
@allure.story('open_weather_map')
def test_owp_weather(get_api_key_from_file):
    params = {'id': str(CITY_ID), 'appid': get_api_key_from_file}
    response = requests.get(BASE_URL, params)
    current_weather = response.json()['weather'][0]
    assert str(current_weather.get('description')) == EXPECTED_WEATHER
