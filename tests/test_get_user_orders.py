import requests
import allure
from data import Urls
from data import ApiAnswer


class TestGetUserOrders:
    @allure.title('Получение заказов конкретного пользователя')
    @allure.description("Авторизованный пользователь, проверка кода и текста ответа")
    def test_get_orders_with_authorization(self, user_token):
        token = user_token
        headers = {'Authorization': token}
        response = requests.get(Urls.CREATING_AN_ORDER, headers=headers)
        assert response.status_code == 200
        assert ApiAnswer.RESPONSE_SUCCESS in response.text

    @allure.title('Получение заказов конкретного пользователя')
    @allure.description("Неавторизованный пользователь, проверка кода и текста ответа")
    def test_get_orders_without_authorization(self):
        response = requests.get(Urls.CREATING_AN_ORDER)
        assert response.status_code == 401
        assert ApiAnswer.ERROR_401_UNAUTHORIZED == response.text
