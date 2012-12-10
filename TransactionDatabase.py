from __future__ import division
from collections import namedtuple, defaultdict
import csv


class Transaction(object):
    def __init__(self, id, itemset, label):
        self.id = id
        self.itemset = itemset
        self.label = label

    def __repr__(self):
        return "Transaction(id={0}, itemset={1}, label={2})".format(self.id, self.itemset, self.label)

    def contains(self, pattern):
        """
        Returns true if the itemset of this transactions contains the given pattern.
        """
        # Slow way to check if the itemset contains the pattern, but works
        # If intersection of pattern and itemset equals the pattern,
        # we can be sure that this transaction is covered by the pattern
        pattern_set = set(pattern)
        itemset_set = set(self.itemset)
        return (itemset_set.intersection(pattern_set) == pattern_set)


class TransactionDatabase(object):
    """
    Class for storing transactions.
    """
    def __init__(self, supportive_label="1"):
        # List of Transactions
        self.transactions = []
        self.itemSupportDict = defaultdict(lambda: 0)
        self.labelSupportiveSymbol = supportive_label

    def buildConditionalDatabase(self, pattern):
        """
        Returns a new TransactionDatabase object with
        only transactions that contain the given pattern.
        """
        condDatabase = TransactionDatabase()

        condDatabase.labelSupportiveSymbol = self.labelSupportiveSymbol

        for transaction in self.transactions :
            if transaction.contains(pattern):
                condDatabase.transactions.append(transaction)

        return condDatabase

    def transactionListFromPattern(self,pattern) :
        transactionList = []

        for transaction in self.transactions :
            # See buildConditionalDatabase
            if transaction.contains(pattern):
                transactionList.append(transaction.id)

        return transactionList

    def size(self):
        return len(self.transactions)

    def __len__(self):
        # Magic method for len() support
        return len(self.transactions)

    def labelSupport(self):
        count = 0

        for transaction in self.transactions :
            if(transaction.label == self.labelSupportiveSymbol):
                count += 1

        return count/len(self)

    def labelAndPatternSupport(self, pattern):
        count = 0

        for transaction in self.transactions :
            if(transaction.label == self.labelSupportiveSymbol and transaction.contains(pattern)):
                count += 1

        return count/len(self)

    def patternSupport(self,pattern):
        count = 0

        for transaction in self.transactions :
            if transaction.contains(pattern):
                count += 1

        return count/len(self)

    def removeTransactions(self, transaction_ids):
        """
        Removes all transactions from the database that are found in the given id list.
        """
        self.transactions = filter(lambda t: t.id not in transaction_ids, self.transactions)

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
        a,b,c...,label
        """
        database = TransactionDatabase()

        for i, line in enumerate(csv.reader(open(filename))):
            t = Transaction(i, line[:-1], line[-1])
            database.add(t)

        return database

    def __repr__(self):
        return "\n".join([repr(transaction) for transaction in self.transactions])

    def __iter__(self):
        for transaction in self.transactions:
            yield transaction
