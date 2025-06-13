import unittest
from digit import Digit

class TestDigit(unittest.TestCase):

    def setUp(self):
        self.digit= Digit(100)

    def test_get_set_value(self):
        self.digit.set_value(40)
        self.assertEqual(self.digit.get_value(), 40)

    def test_to_octal(self):
        self.digit.set_value(40)
        self.assertEqual(self.digit.to_octal(), '0o50')

    def test_to_hex(self):
        self.digit.set_value(40)
        self.assertEqual(self.digit.to_hex(), '0x28')

    def test_to_binary(self):
        self.digit.set_value(40)
        self.assertEqual(self.digit.to_binary(), '0b101000')
if __name__ == '__main__':
    unittest.main()
