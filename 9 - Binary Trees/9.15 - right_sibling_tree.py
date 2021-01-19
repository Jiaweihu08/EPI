"""
Compute the right sibling tree
"""
# class BinaryTreeNode:
# 	def __init__(self, data=0, left=None, right=None):
# 		self.data = data
# 		self.left = left
# 		self.right = right
# 		self.next = None


# def build_binary_tree(values, children):
# 	nodes = [BinaryTreeNode(val) for val in values]
# 	for i in range(len(children)):
# 		if children[i][0] != None:
# 			nodes[i].left = nodes[children[i][0]]
# 		if children[i][1] != None:
# 			nodes[i].right = nodes[children[i][1]]
# 	return nodes[0]


def construct_right_sibling(tree):
	def populate_children_next_field(start_node):
		while start_node and start_node.left:
			start_node.left.next = start_node.right
			# assign start_node.right.next to start_node.next.left
			# if start_node.next, otherwise its assigned to start_node.next
			# which is None
			start_node.right.next = start_node.next and start_node.next.left
			start_node = start_node.next

	while tree and tree.left:
		populate_children_next_field(tree)
		tree = tree.left


# values = range(15)
# children = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]
# tree = build_binary_tree(values, children)
# construct_right_sibling(tree)