import unittest
from kalkulators import saskaitit


class TestKalkulators(unittest.TestCase):
    def test_saskaitit(self):
        rezultats = saskaitit(3, 3)
        self.assertEqual(rezultats, 5)