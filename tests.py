import random
import unittest
from TransactionDatabase import TransactionDatabase, Transaction

class TransactionTestCase(unittest.TestCase):
    def test_contains(self):
        t = Transaction(1, [1, 2, 3], 0)
        # Contains both
        self.assertTrue(t.contains([2, 3]))
        # Contains one
        self.assertTrue(t.contains([2]))
        # Does not contain at all
        self.assertFalse(t.contains([4]))
        # Contains one
        self.assertFalse(t.contains([3, 4]))

if __name__ == '__main__':
    unittest.main()
