import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get(self):
        self.assertEqual(dicts.get_val({0: 1}, 0), 1)
        self.assertEqual(dicts.get_val({0: "zero"}, 0), "zero")
        self.assertEqual(dicts.get_val({0: [1, 2, 3]}, 0), [1, 2, 3])
        self.assertEqual(dicts.get_val({0: [1, "two", (3, 2, 1)]}, 0), [1, "two", (3, 2, 1)])
        self.assertEqual(dicts.get_val(
            {0: "one", "two": [4, 6, 8], 3: (5, 7, 9), "ten": True, (10, 20, 30): 60, (110, 120, 130): 'dozens'}, 3),
            (5, 7, 9))
        self.assertEqual(dicts.get_val(
            {0: "one", "two": [4, 6, 8], 3: (5, 7, 9), "ten": True, (10, 20, 30): 60, (110, 120, 130): 'dozens'},
            'ten'), True)
        self.assertEqual(dicts.get_val(
            {0: "one", "two": [4, 6, 8], 3: (5, 7, 9), "ten": True, (10, 20, 30): 60, (110, 120, 130): 'dozens'},
            (10, 20, 30)), 60)
        self.assertEqual(dicts.get_val({}, 0), "git")
