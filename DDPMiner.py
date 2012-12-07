# encoding: utf-8
from fptree import FPNode, FPTree

class DDPMine:
    """
    Main class implementing the DDPMine algorithm.
    """
    
    def __init__(self, transactionDatabase):
        pass
        self.fp_tree = FPTree()
        self._maxGain_ = 0.0
        self._globalTransactionDatabase = transactionDatabase;
        self._bestPatterns = []

    #need to decide whether to do this recursivly or not
    def mine(self):
        """
        Does the heavy lifting of mining for the nodes – returns the list of most
        discriminative patterns.
        """
        bestPattern = branchAndBound(self.fp_tree,s,null)
        if bestPattern = None:
            return
        transactionList = self._globalTransactionDatabase.transactionListFromPattern(bestPattern)
        updatedTree = self.fp_tree.updateTree(transactionList)
        self._bestPatterns.append(mine())
        
    
    def buildTree(transactionDatabase):
    
        self._globalTransactionDatabase = transactionDatabase;
    
        master = FPTree()
        for transaction in transactionDatabase:
            master.add(transaction)
            
    
    def branchAndBound(tree,support,prefix):
        
        for item, nodes in tree.items():
            
            #make sure the support is sufficient
            support = sum(n.count for n in nodes)
            if support >= minimum_support and item not in suffix:
                #we found a new possible canidate
                found_set = [item] + suffix
                
                #since we are looking for the best pattern globally we need to compute the pattern's global information gain thus
                #we use the global transaction database (this is how we get around creating the conditional database right away)
                #complexity of this step is 2N where N is size of global database
                infoGain = UtilityMethods.InformationGain(self._globalTransactionDatabase.patternSupport(found_set),self._globalTransactionDatabase.labelSupport(),self._globalTransactionDatabase.labelSupport(found_set))
                
                #if it is the best pattern then save it
                if infoGain > self._maxGain_ :
                    self._maxGain_ = infoGain
                    bestPattern = found_set
                
                #construct the conditional database of new canidate from the global database
                #complexity of this step is probably N
                conditionDatabase = self._globalTransactionDatabase.buildConditionalDatabase(self, found_set)
                
                #compute the information gain upperbound of this new conditional database based on the size of the conditional database and the global label support
                #complexity of this step should be 1
                infoGainBound = UtilityMethods.InformationGainUpperBound(conditionalDatabase.size()/self._globalTransactionDatabase.size(),self._globalTransactionDatabase.labelSupport())    
                
                #if potential for high information gain patterns then recursivly mine them
                if self._maxGain_ >= infoGainBound :
                    pass
                else :
                # Build a conditional tree and recursively mine
                    conditionalTree = conditional_tree_from_paths(tree.prefix_paths(item),minimum_support)
                    branchAndBound(conditionalTree,support,item)
