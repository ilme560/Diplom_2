class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'
    GET_INGREDIENTS = f'{URL}/api/ingredients'
    CREATING_AN_ORDER = f'{URL}/api/orders'
    CREATING_A_USER = f'{URL}/api/auth/register'
    USERS_LOGIN = f'{URL}/api/auth/login'
    CHANGING_USER_DATA = f'{URL}/api/auth/user'


class Ingredients:
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    WITHOUT_INGREDIENTS = {"ingredients": []}
    INCORRECT_INGREDIENTS = payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d1", "61c0c5a71d1f82001bdaaa701"]}
    BUN_R2_D3 = '61c0c5a71d1f82001bdaaa6d'
    MAIN_PROTOSTOMIA = '61c0c5a71d1f82001bdaaa6f'
    SAUSE_SPICY_X = '61c0c5a71d1f82001bdaaa72'
    INCORRECT_INGTEDIENTS = '61c0c5a71d1f82001bdaaa72test'


class ApiAnswer:
    ERROR_400_BAD_REQUEST = '{"success":false,"message":"Ingredient ids must be provided"}'
    ERROR_401_INCORRECT = '{"success":false,"message":"email or password are incorrect"}'
    ERROR_401_UNAUTHORIZED = '{"success":false,"message":"You should be authorised"}'
    ERROR_403_EXISTING = '{"success":false,"message":"User already exists"}'
    ERROR_403_FORBIDDEN = '{"success":false,"message":"Email, password and name are required fields"}'
    ERROR_500_INTERNAL_SERVER_ERROR = "Internal Server Error"

    RESPONSE_SUCCESS = '"success":true'
    RESPONSE_SUCCESS_LOGIN = '"refreshToken"'
