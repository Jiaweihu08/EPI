"""
Given a BST and a value k, return the first key from the tree
that's greater than k in sorted order.
"""
def find_first_greater_than_k_inorder(tree, k):
	"""
	Perform inorder traversal and return the first
	node whose key is greater than k.

	O(n) time complexity.
	O(1) space complexity.
	"""
	def inorder_traversal(tree):
		if not tree:
			return None

		left_val = inorder_traversal(tree.left)
		if left_val:
			return left_val

		if tree.data > k:
			return tree
		return inorder_traversal(tree.right)
	return inorder_traversal(tree)


def find_first_greater_than_k(tree, k):
	"""
	Improve efficiency by performing binary search.

	O(h) time complexity
	O(1) space complexity
	"""
	subtree, first_so_far = tree, None
	while subtree:
		if subtree.data > k:
			first_so_far, subtree = subtree, subtree.left
		else:
			subtree = subtree.right
	return first_so_far

