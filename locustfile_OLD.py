import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.post("/predict HTTP/1.1")
        self.client.get("/world")

#    @task(3)
#    def view_item(self):
#        for item_id in range(10):
#            self.client.get("/")
#            time.sleep(1)

#   def on_start(self):
#        self.client.post("/login", json={"username":"foo", "password":"bar"})