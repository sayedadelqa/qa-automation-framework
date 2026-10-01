import requests
from utils.config import API_BASE_URL


class ApiClient:
    """Small wrapper around requests so tests stay short and readable."""

    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, path: str, **kwargs):
        return self.session.get(f"{self.base_url}{path}", timeout=15, **kwargs)

    def post(self, path: str, payload: dict):
        return self.session.post(f"{self.base_url}{path}", json=payload, timeout=15)

    def put(self, path: str, payload: dict):
        return self.session.put(f"{self.base_url}{path}", json=payload, timeout=15)

    def delete(self, path: str):
        return self.session.delete(f"{self.base_url}{path}", timeout=15)
