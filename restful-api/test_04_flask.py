import unittest
import requests

class TestFlaskAPI(unittest.TestCase):
    base_url = "http://localhost:5000"

    def test_home(self):
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_data(self):
        response = requests.get(f"{self.base_url}/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_user(self):
        user = {"username": "alice", "name": "Alice", "age": 25, "city": "San Francisco"}
        response = requests.post(f"{self.base_url}/add_user", json=user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "User added")
        self.assertEqual(response.json()["user"], user)

    def test_get_user(self):
        # Ensure the user "jane" is added before testing
        user = {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}
        requests.post(f"{self.base_url}/add_user", json=user)
        response = requests.get(f"{self.base_url}/users/jane")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "jane")

    def test_get_nonexistent_user(self):
        response = requests.get(f"{self.base_url}/users/nonexistent")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_status(self):
        response = requests.get(f"{self.base_url}/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_add_user_without_username(self):
        user = {"name": "Alice", "age": 25, "city": "San Francisco"}
        response = requests.post(f"{self.base_url}/add_user", json=user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Username is required")

    def test_add_duplicate_user(self):
        user = {"username": "alice", "name": "Alice", "age": 25, "city": "San Francisco"}
        response = requests.post(f"{self.base_url}/add_user", json=user)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()["error"], "User already exists")

if __name__ == "__main__":
    unittest.main()
    