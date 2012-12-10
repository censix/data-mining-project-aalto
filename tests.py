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

class TransactionDatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.database = TransactionDatabase(1)
        self.database.add(Transaction(1, [1,2,3], 0))
        self.database.add(Transaction(2, [2,3,4], 1))
        self.database.add(Transaction(3, [1], 0))
        self.database.add(Transaction(4, [2], 1))
        self.database.add(Transaction(5, [2,3, 5], 1))

    def test_len(self):
        self.assertEquals(len(self.database), 5)

    def test_buildConditionalDatabase(self):
        cond_db = self.database.buildConditionalDatabase([1])
        self.assertEquals(len(cond_db), 2)

    def test_transactionListFromPattern(self):
        tlist = self.database.transactionListFromPattern([1])
        self.assertEquals(tlist, [1, 3])

    def test_labelSupport(self):
        self.assertEquals(self.database.labelSupport(), 0.6)

    def test_labelAndPatternSupport(self):
        # All matched
        self.assertEquals(self.database.labelAndPatternSupport([2]), 0.6)
        # One matched
        self.assertEquals(self.database.labelAndPatternSupport([5]), 0.2)

    def test_patternSupport(self):
        self.assertEquals(self.database.patternSupport([2,3,5]), 0.2)

    def test_removeTransactions(self):
        self.database.removeTransactions([3, 5])
        self.assertEquals(len(self.database), 3)

    def test_cleanAndPrune(self):
        # Not needed anymore? Add tests later
        pass


if __name__ == '__main__':
    unittest.main()
