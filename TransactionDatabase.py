from collections import namedtuple

# This behaves like a class:
# my_transaction = Transaction(id=2, itemset=['a','b','c'], label=1)
# my_transaction.id == 2
# my_transaction.itemset == ['a','b','c']
Transaction = namedtuple("Transaction", "id, itemset, label")

class TransactionDatabase(object):
    """
    Class for storing transactions.
    """
    def __init__(self):
        # List of Transactions
        self.transactions = []

    def buildConditionalDatabase(self, pattern):
        """
        Returns a new TransactionDatabase object with
        only transactions that contain the given pattern.
        """
        pass

    def labelSupport(self):
        pass

    def labelSupport(self, pattern):
        """
        Label / transaction union support
        """
        pass

    def removeTransactions(self, pattern):
        """
        Removes all transactions from the database that match the given pattern.
        """
        pass
