import requests
from requests import Response
from bookstore.models import UserModel, TokenModel


BASE_URL = 'https://demoqa.com'
ACCOUNT_URL = BASE_URL + '/Account/v1'


def create_user(username, password) -> UserModel:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_URL}/User', json=payload)
    if response.ok:
        return UserModel(**response.json())
    else:
        # if response is not ok, raise an error. Maybe a ValueError, ConnectionError, or your own custom error!
        raise ValueError(f'Unable to create user: {response.content}')


def generate_token(username, password) -> TokenModel:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_URL}/GenerateToken', json=payload)
    if response.ok:
        return TokenModel(**response.json())
    else:
        raise ValueError(f'Unable to generate token: {response.content}')


def delete_user(user_id, token) -> Response:
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f'{ACCOUNT_URL}/User/{user_id}', headers=headers)
    if response.ok:
        return response
    else:
        raise ValueError(f'Unable to delete user: {response.content}')


def is_authorized(username, password) -> bool:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_URL}/Authorized', json=payload)

    # we can also write our if/else block this way
    if not response.ok:
        raise ConnectionError(f'Unable to authorize user: {response.content}')

    return response.json()
