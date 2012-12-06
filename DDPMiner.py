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

    def mine(self):
        """
        Does the heavy lifting of mining for the nodes – returns the list of most
        discriminative patterns.
        """
        pass
    
    def buildTree(transactionDatabase):
    
        master = FPTree()
        for transaction in transactionDatabase:
            master.add(transaction)
            
            
    #Procedure branch and bound(P; s; ?)
    #1: if P = ?
    #2: return;
    #3: for each item ai in P do
    #4: generate pattern ? = ai [ ? with support=ai.support;
    #5: compute information gain IG(?);
    #6: if IG(?) > maxIG
    #7: maxIG := IG(?);
    #8: bestP at := ?;
    #9: construct pattern ?'s conditional database D?;
    #10: IGub(jD?j) := upper bound(jD?j);
    #11: if maxIG ? IGub(D?)
    #12: skip mining on D?;
    #13: else
    #14: construct ?'s conditional FP-tree P?;
    #15: branch and bound(P?; s; ?);
    
    def branchAndBound(tree,support,prefix,database):
        
        for item, nodes in tree.items():
            
            support = sum(n.count for n in nodes)
            if support >= minimum_support and item not in suffix:
                # New winner!
                found_set = [item] + suffix
                yield (found_set, support) if include_support else found_set
                
                #TODO: construct conditional database
                cond_database = None
                
                infoGain = UtilityMethods.InformationGain(patternSupport,labelSupport,patternLabelUnionSupport)
                
                if infoGain > self._maxGain_ :
                    self._maxGain_ = infoGain
                    bestPattern = found_set
                
                infoGainBound = UtilityMethods.InformationGainUpperBound(potentialSupport,labelSupport)    
                
                if self._maxGain_ >= infoGainBound :
                    pass
                else :
                # Build a conditional tree and recursively search for frequent
                # itemsets within it.
                    cond_tree = conditional_tree_from_paths(tree.prefix_paths(item),minimum_support)
                    branchAndBound(cond_tree,support,item,cond_database)
