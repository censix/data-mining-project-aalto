from DDPMiner import DDPMine
from fptree import FPTree
from TransactionDatabase import TransactionDatabase

def run_ddpmine():
    # Just some placeholder data
    miner = DDPMine(["a", "b"])
    miner.mine()

if __name__ == "__main__":
    
    database = TransactionDatabase.loadFromFile("test.csv")
    database.cleanAndPrune(2)
    
    miner = DDPMine()
    print miner.mine(database,0)
    
    """
    database = TransactionDatabase.loadFromFile("test.csv")
    database.cleanAndPrune(2)
    print "Cleaned database:"
    print database
    print "\nItems in FP tree and corresponding nodes:"
    tree = FPTree()
    for t in database:
        tree.add(t)

    print str(tree)
    #run_ddpmine()
    """