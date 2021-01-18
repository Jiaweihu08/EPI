"""
Given node from a binary tree, compute its successor.
"""
def find_successor(node):
	if node.right:
		# find the left-most node in its right tree
		node = node.right
		while node.left:
			node = node.left
		return node

	# find the first node whose left subtree contains
	# this node
	while node.parent and node is node.parent.right:
		node = node.parent
	return node.parent

