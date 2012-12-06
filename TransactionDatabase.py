from collections import namedtuple, defaultdict
import csv


class Transaction(object):
    def __init__(self, id, itemset, label):
        self.id = id
        self.itemset = itemset
        self.label = label

    def __repr__(self):
        return "Transaction(id={0}, itemset={1}, label={2})".format(self.id, self.itemset, self.label)


class TransactionDatabase(object):
    """
    Class for storing transactions.
    """
    def __init__(self):
        # List of Transactions
        self.transactions = []
        self.itemSupportDict = defaultdict(lambda: 0)

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
        # Prune out infrequent items
        self.itemSupportDict = dict((item, support) for item, support in self.itemSupportDict.iteritems() if support >= minsup)

        # sorted in decreasing order of frequency.
        # Function to clean transaction from
        def clean_transaction(transaction):
            transaction.itemset = filter(lambda v: v in self.itemSupportDict, transaction.itemset)
            transaction.itemset.sort(key=lambda v: self.itemSupportDict[v], reverse=True)
            return transaction

        for i, transaction in enumerate(self.transactions):
            self.transactions[i] = clean_transaction(transaction)

    def add(self, transaction):
        """
        Adds a new transaction to this transaction database.
        """
        self.transactions.append(transaction)
        for item in transaction.itemset:
            self.itemSupportDict[item] += 1

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
