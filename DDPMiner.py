# encoding: utf-8
from fptree import FPNode, FPTree
from utility_methods import UtilityMethods

class DDPMine:
    """
    Main class implementing the DDPMine algorithm.
    """
    
    def __init__(self):
        self.fp_tree = FPTree()
        self._maxGain_ = 0.0
        self._bestPattern = None
        self._bestPatterns = []

    def mine(self,transactionDatabase,support):
        self._globalTransactionDatabase = transactionDatabase
        self.fp_tree = self.buildTree(transactionDatabase)
        
        return self._mine(self.fp_tree,support)

    def _mine(self,P,s):
        """
        Does the heavy lifting of mining for the nodes – returns the list of most
        discriminative patterns.
        """
        #while the tree is not empty 
        while not P.empty :
            
            #branch and bound to find best pattern
            self.branchAndBound(P,s,[])
            
            print "best pattern:"
            print self._bestPattern
            
            #if no best pattern then break
            if self._bestPattern == None:
                break
            
            #get transaction list and update tree
            transactionList = self._globalTransactionDatabase.transactionListFromPattern(self._bestPattern)
            
            P.updateTree(transactionList)
            
            #append the new best found pattern
            self._bestPatterns.append(self._bestPattern)
            
            #reset the best pattern
            self._bestPattern = None
            self._maxGain_ = 0
            
        #return the list of best patterns
        return self._bestPatterns
    
    def buildTree(self,transactionDatabase):
        
        master = FPTree()
        for transaction in transactionDatabase:
            master.add(transaction)
            
        return master
    
    def branchAndBound(self,tree,minimum_support,suffix):
        
        for item, nodes in tree.items():
            
            #make sure the support is sufficient
            support = sum(n.count for n in nodes)
            if support >= minimum_support and item not in suffix:
                #we found a new possible canidate
                found_set = [item] + suffix
                print "found set:"
                print found_set
                
                #since we are looking for the best pattern globally we need to compute the pattern's global information gain thus
                #we use the global transaction database (this is how we get around creating the conditional database right away)
                #complexity of this step is 2N where N is size of global database
                infoGain = UtilityMethods.InformationGain(self._globalTransactionDatabase.patternSupport(found_set),self._globalTransactionDatabase.labelSupport(),self._globalTransactionDatabase.labelAndPatternSupport(found_set))
                print "info gain:"
                print infoGain
                
                #if it is the best pattern then save it
                if infoGain > self._maxGain_ :
                    self._maxGain_ = infoGain
                    self._bestPattern = found_set
                
                #construct the conditional database of new canidate from the global database
                #complexity of this step is probably N
                conditionalDatabase = self._globalTransactionDatabase.buildConditionalDatabase(found_set)
                
                #compute the information gain upperbound of this new conditional database based on the size of the conditional database and the global label support
                #complexity of this step should be 1
                infoGainBound = UtilityMethods.InformationGainUpperBound(conditionalDatabase.size()/self._globalTransactionDatabase.size(),self._globalTransactionDatabase.labelSupport())    
                
                #if potential for high information gain patterns then recursivly mine them
                if self._maxGain_ >= infoGainBound :
                    pass
                else :
                # Build a conditional tree and recursively mine
                    conditionalTree = conditional_tree_from_paths(tree.prefix_paths(item),minimum_support)
                    branchAndBound(conditionalTree,minimum_support,item)
