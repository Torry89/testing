import unittest
from main_1_1 import solution


class TestMain(unittest.TestCase):
    def test_discriminant(self):
       params = ((1, 8, 15, -5),
                 (1, -13, 12, 1),
                 (-4, 28, -49, 3.5),
                 (1, 1, 1, "корней нет")
                 )
       for i,(a,b,c,expected) in enumerate(params):
           with self.subTest(i):
               result = solution(a,b,c)
               self.assertEqual(expected,result)
