import allure
import requests
import constants


@allure.feature('status200_check')
@allure.story('open_weather_map')
def test_owp_status(get_api_key_from_file):
    params = {'id': str(constants.CITY_ID), 'appid': get_api_key_from_file}
    response = requests.get(constants.BASE_URL, params)
    assert response.status_code == 200


@allure.feature('weather_check')
@allure.story('open_weather_map')
def test_owp_weather(get_api_key_from_file):
    params = {'id': str(constants.CITY_ID), 'appid': get_api_key_from_file}
    response = requests.get(constants.BASE_URL, params)
    current_weather = response.json()['weather'][0]
    assert str(current_weather.get('description')) == constants.EXPECTED_WEATHER
