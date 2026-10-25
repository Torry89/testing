from uuid import uuid4
import requests
import pytest

from settings import YD_token

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

@pytest.fixture
def token():
    token = YD_token
    if not token:
        pytest.fail("Yandex_disk токена нет в переменных окружения")
    return token

@pytest.fixture
def headers(token):
    return  {'Authorization': f'OAuth {token}'}

@pytest.fixture
def temp_folder():
    return f'test-folder-{uuid4()}'

@pytest.fixture
def create_and_cleanup_folder(headers,temp_folder):
    folder_path = f"disk:/{temp_folder}"
    response = requests.put(BASE_URL, headers=headers, params={'path': folder_path})
    assert response.status_code in [201, 409], f"Ошибка при создании: {response.text}"
    yield temp_folder
    requests.delete(BASE_URL, headers=headers, params={'path': folder_path, 'permanently': 'true'})


def test_create_folder_YD_success(headers,temp_folder):
    response = requests.put(BASE_URL,headers=headers,params={'path':f'disk/{temp_folder}'})
    assert response.status_code in [201,409]

def test_create_existing_folder_YD(headers,create_and_cleanup_folder):
    folder = create_and_cleanup_folder
    response = requests.put(BASE_URL,headers=headers,params={'path':f'disk/{folder}'})
    assert response.status_code == 409

def test_create_folder_invalid_path(headers):
     response = requests.put(BASE_URL, headers=headers, params={'path': 'disk://///'})
     assert response.status_code == 404