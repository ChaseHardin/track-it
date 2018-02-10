from app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping_status_code(self):
        result = self.app.get('/ping')
        self.assertEqual(result.status_code, 200)

    def test_ping_message(self):
        result = self.app.get('/ping')
        self.assertEqual(result.data, "Service is Healthy")
