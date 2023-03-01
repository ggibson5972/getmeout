import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


def test_get_url_basic(api_client):
    url = "http://127.0.0.1:8000/events/"
    response = api_client.get(url)
    assert response.status_code == 200


def test_get_url_query(api_client):
    url = "http://127.0.0.1:8000/events/?zipcode=43147"
    response = api_client.get(url)
    assert response.status_code == 200


def test_get_url_missing_zipcode(api_client):
    url = "http://127.0.0.1:8000/events/?zipcode="
    response = api_client.get(url)
    assert response.status_code == 200
