import unittest

from faker import Faker
from app import app

class testApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_sum(self):
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        payload = {"num1": num1, "num2": num2}
        response = self.app.post('/sum', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], num1 + num2)
    
if __name__ == '__main__':
    unittest.main()
    
