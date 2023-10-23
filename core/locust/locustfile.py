from locust import HttpUser, task

class QuickstartUser(HttpUser):

    def on_start(self):
        response = self.client.post('/accounts/api/v1/jwt/create/',data={
            "email":"todo@todo.com",
            "password":"123",
        }).json()
        self.client.headers = {'Authorization':f"Bearer {response.get('access',None)}"}
    
    @task
    def task_list(self):
        self.client.get("/task/api/v1/task/")