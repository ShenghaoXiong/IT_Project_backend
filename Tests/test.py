import sys
sys.path.append('../')
import unittest
from unittest.mock import patch
from app import app  # This should now work
# Mocking the database model for testing, replace this with your actual database model
class MockModel:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Test case for the Flask app's CRUD operations
class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Setting up the app for testing
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('app.Plants', new_callable=lambda: MockModel)  # Mocking the Plants model
    def test_get_plants(self, MockModel):
        # Testing the GET operation for plants
        response = self.app.get('/plants')
        self.assertEqual(response.status_code, 200)

    @patch('app.Plants', new_callable=lambda: MockModel)  # Mocking the Plants model
    def test_create_plant(self, MockModel):
        # Testing the POST operation for plants
        response = self.app.post('/plants', json={
            'idGarden': 1,
            'plantsName': 'Rose',
            'plantType': 'Flower',
            'plantDay': 'Monday',
            'plantXpoint': 50,
            'plantYpoint': 50,
            'radius': 10
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Rose', response.data)

    @patch('app.Resource', new_callable=lambda: MockModel)  # Mocking the Resource model
    def test_get_resources(self, MockModel):
        # Testing the GET operation for resources
        response = self.app.get('/resource')
        self.assertEqual(response.status_code, 200)

    @patch('app.Weeds', new_callable=lambda: MockModel)  # Mocking the Weeds model
    def test_create_weed(self, MockModel):
        # Testing the POST operation for weeds
        response = self.app.post('/weeds', json={
            'weedXpoint': 50,
            'weedYpoint': 50,
            'weedSize': 5,
            'idLand': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'weed', response.data.lower())

# Running the tests
if __name__ == '__main__':
    unittest.main()
