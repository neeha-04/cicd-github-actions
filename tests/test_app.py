import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    assert client.get('/').status_code == 200


def test_health_endpoint(client):
    response = client.get('/health', headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'


def test_health_has_timestamp(client):
    data = client.get('/health', headers={'Accept': 'application/json'}).get_json()
    assert 'timestamp' in data


def test_info_endpoint(client):
    data = client.get('/api/info', headers={'Accept': 'application/json'}).get_json()
    assert data['app'] == 'CI/CD Demo Application'
    assert 'python_version' in data


def test_pipeline_status(client):
    data = client.get('/api/pipeline-status', headers={'Accept': 'application/json'}).get_json()
    assert data['status'] == 'all passing'
    assert 'stages' in data


def test_404_page(client):
    assert client.get('/this-does-not-exist').status_code == 404