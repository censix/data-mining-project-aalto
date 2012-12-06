from collections import namedtuple, defaultdict
import csv

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
        self.itemCounter = defaultdict(lambda: 0)

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

    def cleanAndPrune(self, minsup):
        """
        Cleans transactions from items which don't have support over given minsup.

        Also rearranges itemsets in transactions so that they are in sorted order by
        the support count of items.
        """
        pass

    def add(self, transaction):
        """
        Adds a new transaction to this transaction database.
        """
        self.transactions.append(transaction)
        for item in transaction.itemset:
            self.itemCounter[item] += 1

    @staticmethod
    def loadFromFile(filename):
        """
        Loads transactions from CSV file of form
        id,itemset,label

        id should be transaction number, itemset contain items separated by a space (like "a b c")
        """
        database = TransactionDatabase()

        for line in csv.reader(open(filename)):
            t = Transaction(line[0], line[1].split(" "), line[2])
            database.add(t)

        return database

    def __repr__(self):
        return "\n".join([repr(transaction) for transaction in self.transactions])

    def __iter__(self):
        for transaction in self.transactions:
            yield transaction
