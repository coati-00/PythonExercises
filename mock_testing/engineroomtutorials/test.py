import mock
import unittest
from simple import add_and_multiply


class MyTestCase(unittest.TestCase):

    @mock.patch('simple.multiply')
    def test_add_and_multiply(self, mock_multiply):
        x = 3
        y = 5
        
        mock_multiply.return_value = 15

        addition, multiple = add_and_multiply(x, y)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

if __name__ == "__main__":
    unittest.main()