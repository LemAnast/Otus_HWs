import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url",
                     default="https://ya.ru",
                     help="This is default request url")
    parser.addoption("--status_code",
                     default=200,
                     help="This is default status code")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def test_yandex(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code
