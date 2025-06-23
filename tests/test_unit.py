import unittest
from models import User

class TestUserModel(unittest.TestCase):
    def test_to_dict(self):
        user = User(id=1, name="Alice")
        self.assertEqual(user.to_dict(), {"id": 1, "name": "Alice"})

if __name__ == '__main__':
    unittest.main()
