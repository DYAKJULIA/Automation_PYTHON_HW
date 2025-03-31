import pytest
import requests

# Базовый URL API
BaseURL = "https://yougile.com"

# Токен для авторизации (необходимо заменить на Ваш реальный токен)
KEY = "1OuBjHwe374ITTrYy20hv1LYUR1b0GpS+boRGs2QCha7SgCx+qcflT0dGvy2I88h"

# Заголовки для запросов
HEADERS = {
    'Authorization': f'Bearer {KEY}',
    'Content-Type': 'application/json'
}

# Фикстура для создания проекта
@pytest.fixture()
def create_project():
    body = {
        'title': 'Создание нового проекта'
    }
    response = requests.post(BaseURL + '/api-v2/projects', json=body, headers=HEADERS)
    assert response.status_code == 201
    project_id = response.json()['id']
    yield project_id

# POST СОЗДАНИЕ ПРОЕКТА
@pytest.mark.positive
def test_create_project_positive():
    body = {
        'title': 'Создание нового проекта'
    }
    response = requests.post(BaseURL + '/api-v2/projects', json=body, headers=HEADERS)
    assert response.status_code == 201
    assert 'id' in response.json()

@pytest.mark.negative
def test_create_project_negative():
    body = {
        'title': ''
    }
    response = requests.post(BaseURL + '/api-v2/projects', json=body, headers=HEADERS)
    assert response.status_code == 400

# PUT ИЗМЕНЕНИЕ ПРОЕКТА
@pytest.mark.positive
def test_update_project_positive(create_project):
    id = create_project
    update_body = {
        'title': 'Изменено название в новом проекте'
    }
    response = requests.put(BaseURL + f'/api-v2/projects/{id}', headers=HEADERS)
    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.negative     # Отсутствие обязательного поля
def test_update_project_negative(create_project):
    id = create_project
    update_body = {
        'title': 'Изменено название в новом проекте'
    }
    response = requests.put(BaseURL + f'/api-v2/projects/', headers=HEADERS)
    assert response.status_code == 404

# GET ПОЛУЧЕНИЕ ПРОЕКТА ПО ID
@pytest.mark.positive
def test_get_project_positive(create_project):
    id = create_project
    response = requests.get(BaseURL + f'/api-v2/projects/{id}', headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == id
    assert "id" in response.json()

@pytest.mark.negative     # Получение несуществующего проекта
def test_get_project_negative():
    non_existent_id = "non_existent_id"
    response = requests.get(BaseURL + f'/api-v2/projects/{non_existent_id}', headers=HEADERS)
    assert response.status_code == 404
