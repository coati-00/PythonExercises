'''True unit tests only care that an individual function should work the way
if is supposed to, does not matter what other functions do. In this case if our
function is add_and_multiply we only care that it correctly called the method
with the correct arguments '''

import mock
import unittest
from simple import add_and_multiply


class MyTestCase(unittest.TestCase):
    '''Use mock to replace and simulate inner function multiply, and then
    pass it as an argument to our test. In the context of that particular
    test, any calls to multiply will be replaced/redirected with a call
    to mock. In order for a mock method to return anything you must declare
    a return value for the mocked function - this is what is returned when your
    mock function is called.
    In this case
    your unit test should be testing your function and your function alone'''

    @mock.patch('simple.multiply')
    def test_add_and_multiply(self, mock_multiply):
        x = 3
        y = 5
        
        mock_multiply.return_value = 15

        addition, multiple = add_and_multiply(x, y)
        
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

if __name__ == "__main__":
    unittest.main()