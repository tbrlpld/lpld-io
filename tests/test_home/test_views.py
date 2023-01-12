from http import HTTPStatus

from django import test

import pytest


@pytest.mark.django_db
def test_dummy():
    client = test.Client()
    response = client.get("")
    assert response.status_code == HTTPStatus.OK
