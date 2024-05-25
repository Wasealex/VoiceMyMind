import unittest
from app import create_app

class TestRun(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_app_creation(self):
        self.assertIsNotNone(self.app)

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_debug_mode(self):
        self.assertTrue(self.app.debug)

    def test_app_running(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()