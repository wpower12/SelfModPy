import random

MUTATION_CHANCE = 2
LEAF_VAL_MAX = 100

def get_tree( depth ):
	return get_tree_inner( depth )

def get_tree_inner( d ):
	if( d >= 0 ):
		node = get_internal_node()
		node.left  = get_tree_inner( d-1 )
		node.right = get_tree_inner( d-1 )
		return node
	else:
		return get_leaf_node()

# Internal Nodes
class InternalNode:
	def __init__(self):
		self.left  = []
		self.right = []

	def eval(self):
		return self.left.eval()

class Add(InternalNode):
	def eval(self):
		return self.left.eval()+self.right.eval()

class Multiply(InternalNode):
	def eval(self):
		return self.left.eval()*self.right.eval()

# Leaf Nodes
class LeafNode:
	def __init__(self):
		self.val = []

class Num:
	def eval(self):
		return self.val

# Gettng random nodes
def get_internal_node():
	r = random.randrange( 0, 2 )
	if( r == 0 ):
		return Add()
	else:
		return Multiply()

def get_leaf_node():
	node = Num()
	node.val = random.randrange(0, LEAF_VAL_MAX)
	return node

# Modifying Trees
def modify( tree ):
	par = None
	cur = tree
	leg = ""
	while( cur != None ):
		r = random.randrange(0, MUTATION_CHANCE)
		if( r == 0 ):
			if( isinstance( cur, InternalNode ) ):
				node = get_internal_node
				node.left  = cur.left
				node.right = cur.right
				if( par == None ):
	 				return node
				else:
					if( leg == "L" ):
						parent.left = cur
					else:
						parent.right = cur
					return tree
			else:
				# leaf node, new random value
				cur.val = random.randrange(0, LEAF_VAL_MAX)
		else:
			if( isinstance( cur, InternalNode ) ):
				r = random.randrange(0,2)
				if( r == 0 ):
					cur = cur.left
					leg = "L"
				else:
					cur = cur.right
					leg = "R"
			else:
				break
