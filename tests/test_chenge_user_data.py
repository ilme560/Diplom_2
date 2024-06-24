import requests
import allure
from data import Urls
from data import ApiAnswer
from helpers import get_sign_up_date

class TestChengeUserData:
    @allure.title('Изменение данных пользователя')
    @allure.description("Изменение с авторизацией, проверка кода и текста ответа")
    def test_chenge_user_data_with_authorization(self, user_token):
        token = user_token
        payload = get_sign_up_date()
        headers = {'Authorization': token}
        response = requests.patch(Urls.CHANGING_USER_DATA, headers=headers, data=payload)
        assert response.status_code == 200
        assert ApiAnswer.RESPONSE_SUCCESS in response.text

    @allure.title('Изменение данных пользователя')
    @allure.description("Изменение без авторизации, проверка кода и текста ответа")

    def test_chenge_user_data_without_authorization(self):
        payload = get_sign_up_date()
        response = requests.patch(Urls.CHANGING_USER_DATA, data=payload)
        assert response.status_code == 401
        assert ApiAnswer.ERROR_401_UNAUTHORIZED in response.text
