import unittest

from app import main 

class TestApp(unittest.TestCase):

    def test_string_return(self):
        result = read_root()
        self.assertEqual(result, '<h1>Hello, World!</h1>')

if __name__ == "__main__":
    unittest.main()
