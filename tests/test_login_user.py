import allure
import requests
from data import Urls, ApiAnswer


class TestLoginUser:

    @allure.title('Логин пользователя')
    @allure.description("Проверка логин под существующим пользователем,проверка кода и текста ответа ")
    def test_login_user(self, user_data):
        payload = user_data
        response = requests.post(Urls.USERS_LOGIN, data=payload)
        assert response.status_code == 200
        assert ApiAnswer.RESPONSE_SUCCESS_LOGIN in response.text

    @allure.title('Логин пользователя')
    @allure.description("Проверка логин с неверным паролем пользователя,проверка кода и текста ответа")
    def test_login_user_incorrect_password(self, user_data):
        payload = user_data
        del payload["password"]
        response = requests.post(Urls.USERS_LOGIN, data=payload)
        assert response.status_code == 401
        assert ApiAnswer.ERROR_401_INCORRECT

    @allure.title('Логин пользователя')
    @allure.description("Проверка логин с неверным логином пользователя,проверка кода и текста ответа")
    def test_login_user_incorrect_login(self, user_data):
        payload = user_data
        del payload["email"]
        response = requests.post(Urls.USERS_LOGIN, data=payload)
        assert response.status_code == 401
        assert ApiAnswer.ERROR_401_INCORRECT
