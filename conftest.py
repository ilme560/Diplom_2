import pytest
import requests
from helpers import get_sign_up_date
from data import Urls


@pytest.fixture
def user_data():
    payload = get_sign_up_date()
    response = requests.post(Urls.CREATING_A_USER, data=payload)
    token = response.json()['accessToken']

    yield response, payload, token
    requests.delete(Urls.CHANGING_USER_DATA, headers={'Authorization': token})
