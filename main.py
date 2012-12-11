from DDPMiner import DDPMine
from fptree import FPTree
from TransactionDatabase import TransactionDatabase
from optparse import OptionParser

def run_ddpmine():
    # Just some placeholder data
    miner = DDPMine(["a", "b"])
    miner.mine()

if __name__ == "__main__":
    usage = "usage: %prog [options] filename"
    parser = OptionParser(usage)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug")

    (options, args) = parser.parse_args()

    if len(args) != 3:
        parser.error("You must give the filename, label support symbol, and minimum support.")

    print "Mining from file %s..." % args[0]
    print "Using label support symbol %s..." % args[1]
    print "Using support of %s..." % args[2]
    database = TransactionDatabase.loadFromFile(args[0],args[1],int(float(args[2])))

    miner = DDPMine(debug=False)
    print miner.mine(database,int(float(args[2])))

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
