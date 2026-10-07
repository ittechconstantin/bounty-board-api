import os

import requests


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


def request(method: str, path: str, **kwargs):
    """Call the API and return a success flag plus data or an error message."""
    try:
        response = requests.request(method, f"{API_URL}{path}", timeout=10, **kwargs)
        response.raise_for_status()
        if response.status_code == 204:
            return True, None
        return True, response.json()
    except requests.RequestException as exc:
        detail = str(exc)
        if exc.response is not None:
            try:
                detail = exc.response.json().get("detail", detail)
            except ValueError:
                detail = exc.response.text or detail
        return False, detail
