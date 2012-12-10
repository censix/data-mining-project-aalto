from FPNode import FPNode

from collections import defaultdict, namedtuple
from itertools import imap

class FPTree(object):
    """
    An FP tree.

    This object may only store transaction items that are hashable (i.e., all
    items must be valid as dictionary keys or set members).
    """

    Route = namedtuple('Route', 'head tail')

    def __init__(self):
        # The root node of the tree.
        self._root = FPNode(self, None, None)

        # A dictionary mapping items to the head and tail of a path of
        # "neighbors" that will hit every node containing that item.
        self._routes = {}

    @property
    def root(self):
        """The root node of the tree."""
        return self._root
    
    @property
    def empty(self):
        #if the root node has no children then the tree is empty
        return len(self._root._children)==0

    def add(self, transaction):
        """
        Adds a transaction to the tree.
        """

        point = self._root

        last_point = None;

        for item in transaction.itemset:
            next_point = point.search(item)
            if next_point:
                # There is already a node in this tree for the current
                # transaction item; reuse it.
                next_point.increment()
            else:
                # Create a new point and add it as a child of the point we're
                # currently looking at.
                next_point = FPNode(self, item)
                point.add(next_point)

                # Update the route of nodes that contain this item to include
                # our new node.
                self._update_route(next_point)

            point = next_point
            last_point = next_point

        #add the id as the key and the label as the value to a dictionary stored in the node
        last_point.transactions[transaction.id] = transaction.label

    def _update_route(self, point):
        """Add the given node to the route through all nodes for its item."""
        assert self is point.tree

        try:
            route = self._routes[point.item]
            # Same as route.tail.neighbor
            route[1].neighbor = point # route[1] is the tail
            # route[0] means route.head
            self._routes[point.item] = self.Route(route[0], point)
        except KeyError:
            # First node for this item; start a new route.
            self._routes[point.item] = self.Route(point, point)

    def items(self):
        """
        Generate one 2-tuples for each item represented in the tree. The first
        element of the tuple is the item itself, and the second element is a
        generator that will yield the nodes in the tree that belong to the item.
        """
        for item in self._routes.iterkeys():
            yield (item, self.nodes(item))

    def nodes(self, item):
        """
        Generates the sequence of nodes that contain the given item.
        """

        try:
            node = self._routes[item][0]
        except KeyError:
            return

        while node:
            yield node
            node = node.neighbor

    def prefix_paths(self, item):
        """Generates the prefix paths that end with the given item."""

        def collect_path(node):
            path = []
            while node and not node.root:
                path.append(node)
                node = node.parent
            path.reverse()
            return path

        return (collect_path(node) for node in self.nodes(item))

    def inspect(self):
        print 'Tree:'
        self.root.inspect(1)

        print
        print 'Routes:'
        for item, nodes in self.items():
            print '  %r' % item
            for node in nodes:
                print '    %r' % node

    def _removed(self, node):
        """Called when `node` is removed from the tree; performs cleanup."""

        head, tail = self._routes[node.item]
        if node is head:
            if node is tail or not node.neighbor:
                # It was the sole node.
                del self._routes[node.item]
            else:
                self._routes[node.item] = self.Route(node.neighbor, tail)
        else:
            for n in self.nodes(node.item):
                if n.neighbor is node:
                    n.neighbor = node.neighbor # skip over
                    if node is tail:
                        self._routes[node.item] = self.Route(head, n)
                    break

    def conditional_tree_from_paths(self,paths,minimum_support):
        """Builds a conditional FP-tree from the given prefix paths."""
        tree = FPTree()
        condition_item = None
        items = set()
    
        # Import the nodes in the paths into the new tree. Only the counts of the
        # leaf notes matter; the remaining counts will be reconstructed from the
        # leaf counts.
        for path in paths:
            if condition_item is None:
                condition_item = path[-1].item
    
            point = tree.root
            for node in path:
                next_point = point.search(node.item)
                if not next_point:
                    # Add a new node to the tree.
                    items.add(node.item)
                    count = node.count if node.item == condition_item else 0
                    next_point = FPNode(tree, node.item, count)
                    point.add(next_point)
                    tree._update_route(next_point)
                point = next_point
    
        assert condition_item is not None
    
        # Calculate the counts of the non-leaf nodes.
        for path in tree.prefix_paths(condition_item):
            count = None
            for node in reversed(path):
                if count is not None:
                    node._count += count
                count = node.count
    
        # Eliminate the nodes for any items that are no longer frequent.
        for item in items:
            support = sum(n.count for n in tree.nodes(item))
            if support < minimum_support:
                # Doesn't make the cut anymore
                for node in tree.nodes(item):
                    if node.parent is not None:
                        node.parent.remove(node)
    
        # Finally, remove the nodes corresponding to the item for which this
        # conditional tree was generated.
        for node in tree.nodes(condition_item):
            if node.parent is not None: # the node might already be an orphan
                node.parent.remove(node)
    
        return tree

    def __repr__(self):
        printable = []
        for item, nodeiterator in self.items():
            printable.append(item)
            for node in nodeiterator:
                printable.append(node)
        return "\n".join([repr(s) for s in printable])

    def UpdateTree(self, transactions):
	"""
	1. Updates the tree and decrements count in the node
	2. Updates the transaction IDs	
	3. Removes node if count is zero
	"""
        
	# Iterate over the transactions
	for transaction in transactions:
		next_point = self.root(self) # Start from the root
		for item in transaction.itemset:
			curr_point = next_point
		        next_point = next_point.search(item) 
			next_point._count -= next_point._count # update the count		       			

			if next_point._count is None: 
				curr_point.remove(curr_point,next_point) 
	        
		# update the transaction ids		
		next_point.transaction = filter(lambda v: transaction.id not in v.id, next_point.transaction)   	



