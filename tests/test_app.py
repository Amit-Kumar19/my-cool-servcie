import unittest
from app import create_app
from flask import json


class MyCoolServiceTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test client and test data.
        """
        self.app = create_app()
        self.client = self.app.test_client()

        # Set up some test tokens
        self.admin_token = "admin-token"
        self.user_token = "user-token"

    def test_get_users_unauthorized(self):
        """
        Test accessing the user list without a token.
        """
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 401)

    def test_get_users_authorized(self):
        """
        Test accessing the user list with a valid token.
        """
        response = self.client.get('/api/users', headers={
            'Authorization': f'Bearer {self.user_token}'
        })
        self.assertEqual(response.status_code, 200)

    def test_create_user_unauthorized(self):
        """
        Test creating a user without a valid token.
        """
        response = self.client.post('/api/users', json={
            'name': 'John Doe',
            'email': 'john@example.com'
        })
        self.assertEqual(response.status_code, 401)

    def test_create_user_authorized(self):
        """
        Test creating a user with a valid admin token.
        """
        response = self.client.post('/api/users', headers={
            'Authorization': f'Bearer {self.admin_token}'
        }, json={
            'name': 'John Doe',
            'email': 'john@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'John Doe')
        self.assertEqual(response.json['email'], 'john@example.com')

    def test_create_user_bad_request(self):
        """
        Test creating a user with missing fields.
        """
        response = self.client.post('/api/users', headers={
            'Authorization': f'Bearer {self.admin_token}'
        }, json={
            'name': 'John Doe'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Bad Request')


if __name__ == '__main__':
    unittest.main()
