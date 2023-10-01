import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_status_200(self):
        client = APIClient()
        url = reverse('task:api-v1:task-list')
        response = client.get(url)
        assert response.status_code == 200