from flask import json
from app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping_status_code(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)

    def test_ping_message(self):
        response = self.app.get('/ping')
        self.assertEqual(response.data, "Service is Healthy")

    def test_get_summary__when_multiple_times_have_been_entered(self):
        expected_response = [
            {
                'id': 1,
                'category': 'merge request',
                'summary': 'trying to get people to review'
            },
            {
                'id': 2,
                'category': 'build is down',
                'summary': 'external team broke build'
            }
        ]

        actual_response = self.app.get('/entry')
        data = json.loads(actual_response.get_data())

        self.assertEqual(actual_response.status_code, 200)
        self.assertEqual(data, expected_response)
