# encoding: utf-8
from fptree import FPNode, FPTree

class DDPMine:
    """
    Main class implementing the DDPMine algorithm.
    """
    def __init__(self, transactionDatabase):
        self.fp_tree = FPTree()
        self.transactionDatabase = transactionDatabase

    def mine(self):
        """
        Does the heavy lifting of mining for the nodes – returns the list of most
        discriminative patterns.
        """
        pass

    def _buildFPTree(self):
        """
        Builds the FPTree from the transaction database.
        """
        pass
