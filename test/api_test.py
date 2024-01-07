from random import choice
from json import dumps

from locust import task
from locust import HttpUser

names = [
    "jack",
    "steve",
    "bob"
]


class MyUser(HttpUser):
    host = f"http://127.0.0.1:9999"

    @task(1)
    def query_test(self):
        header = {"Content-Type": "application/json"}
        data = {"name": choice(names)}
        self.client.post("/test", data=dumps(data), headers=header, verify=False)
