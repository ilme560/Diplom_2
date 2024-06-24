import pytest
import requests
import allure
from helpers import get_sign_up_date
from data import Urls
from data import ApiAnswer


class TestCreateUser:
    @allure.title('Создание пользователя')
    @allure.description("Проверка создать уникального пользователя, проверка кода и текста ответа")
    def test_create_user(self, user_registration):
        response = user_registration
        assert response.status_code == 200
        assert ApiAnswer.RESPONSE_SUCCESS in response.text

    @allure.title("Создание пользователя")
    @allure.description("Проверка создать пользователя, который уже зарегистрирован, проверка кода и текста ответа")
    def test_create_user_twice(self, user_data):
        payload = user_data
        response = requests.post(Urls.CREATING_A_USER, data=payload)
        assert response.status_code == 403
        assert ApiAnswer.ERROR_403_EXISTING in response.text

    @allure.title("Создание пользователя")
    @allure.description(
        "Проверка создать пользователя и не заполнить одно из обязательных полей, проверка кода и текста ответа")
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_without_required_field(self, field):
        payload = get_sign_up_date()
        del payload[field]
        response = requests.post(Urls.CREATING_A_USER, data=payload)
        assert response.status_code == 403
        assert ApiAnswer.ERROR_403_FORBIDDEN in response.text
