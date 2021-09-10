"""
https://docs.pytest.org/en/6.2.x/example/simple.html
"""
import pytest


def pytest_addoption(parser):
    parser.addoption('--develop', action='store_true')


@pytest.fixture
def develop(request):
    return request.config.getoption('--develop')
