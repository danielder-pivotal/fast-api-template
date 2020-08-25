import unittest
from app import main
from fastapi.testclient import TestClient

class UnitTest(unittest.TestCase):

    def test_string_return(self):
        result = main.read_root()
        self.assertEqual(result, "I'm alive")

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(main.app)

    def test_alive(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_version(self):
        response = self.client.get("/db")
        self.assertEqual(response.text, '"PostgreSQL 11.7"')
