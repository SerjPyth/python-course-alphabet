import unittest

from game_app import app


class TestHealthEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/_health')
        self.assertEqual(response.status_code, 200)
