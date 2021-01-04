"""
Given a BST and an integer k, return the k largest values
from the tree
"""
def find_k_largest_values(tree, k):
	"""
	Traverse the tree in inorder fashion and record the values
	return the k last values
	"""
	def inorder_traversal(tree):
		if not tree:
			return
		inorder_traversal(tree.left)
		result.append(tree.data)
		inorder_traversal(tree.right)
	result = []
	inorder_traversal(tree)
	return result[-k:]




