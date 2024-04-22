from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # wait time between requests

    @task
    def test(self):
        self.client.get("/55.5")