import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_status_200(self,api_client):
        url = reverse('task:api-v1:task-list')
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_post_task_response_unauthorized_status_401(self,api_client):
        url = reverse('task:api-v1:task-list')
        data = {
            'title':'Go to the gym',
            'is_done':False,
        }
        response = api_client.post(url,data)
        assert response.status_code == 401