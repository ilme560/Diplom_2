import requests
import allure
from data import Urls
from data import ApiAnswer
from data import Ingredients


class TestCreatingOrder:

    @allure.title('Создание заказа')
    @allure.description("Создание заказа с авторизацией, проверка кода и текста ответа")
    def test_create_order_with_authorization(self, user_data):
        token = user_data
        ingredients = {
            "ingredients": [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(Urls.CREATING_AN_ORDER, headers=headers, json=ingredients)
        assert response.status_code == 200
        assert ApiAnswer.RESPONSE_SUCCESS in response.text

    @allure.title('Создание заказа')
    @allure.description("Создание заказа без авторизации, проверка кода и текста ответа")
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Urls.CREATING_AN_ORDER, headers=headers, json=payload)
        assert response.status_code == 200
        assert ApiAnswer.RESPONSE_SUCCESS in response.text

    @allure.title('Создание заказа')
    @allure.description("Создание заказа без ингредиентов, проверка кода и текста ответа")
    def test_create_order_without_ingredients(self):
        payload = Ingredients.WITHOUT_INGREDIENTS
        response = requests.post(Urls.CREATING_AN_ORDER, data=payload)
        assert response.status_code == 400
        assert ApiAnswer.ERROR_400_BAD_REQUEST in response.text

    @allure.title('Создание заказа')
    @allure.description("Создание заказа с неверным хешем ингредиентов, проверка кода и текста ответа")
    def test_create_order_uncorrected_ingredients(self):
        payload = Ingredients.INCORRECT_INGREDIENTS
        response = requests.post(Urls.CREATING_AN_ORDER, data=payload)
        assert response.status_code == 500
        assert ApiAnswer.ERROR_500_INTERNAL_SERVER_ERROR in response.text
