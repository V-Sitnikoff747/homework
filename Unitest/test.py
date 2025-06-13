import unittest
from mainFile import setNumbers
class TestSet(unittest.TestCase):
    def setUp(self):
        self.set= setNumbers([5,6,7,8,9,10])
        self.empty=setNumbers()

    def test_sumSet(self):
        self.assertEqual(self.set.sumSet(),45)
        self.assertEqual(self.empty.sumSet(),0)

    def test_average(self):
        self.assertEqual(self.set.average(), 7.5)
        self.assertEqual(self.empty.average(), 0)
    
    def test_maxValue(self):
        self.assertEqual(self.set.maxValue(), 10)
        self.assertIsNone(self.empty.maxValue())

    def test_minValue(self):
        self.assertEqual(self.set.minValue(), 5)
        self.assertIsNone(self.empty.minValue())

