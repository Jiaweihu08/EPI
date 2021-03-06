"""
Given a BST and an integer k, return the k largest values from
the tree.
"""
# def find_k_largest_in_bst_naive(tree, k):
# 	"""
# 	Traverse the tree in inorder fashion, record the values and
# 	return the k last values.

# 	O(n) time and space complexity.
# 	"""
# 	def inorder_traversal(tree):
# 		if not tree:
# 			return
# 		inorder_traversal(tree.left)
# 		result.append(tree.data)
# 		inorder_traversal(tree.right)
# 	result = []
# 	inorder_traversal(tree)
# 	return result[-k:]


def find_k_largest_in_bst(tree, k):
	"""
	Reversed inorder traversal yields values from a bst in a 
	nonincreasing order.

	We can perform reverse inorder traversal and append the
	largest value at each step as long as the number of
	values in the result is smaller than k.

	O(h + k) time complexity;
	h = tree height, descending h times, and ascend back k times
	"""
	def find_k_largest_in_bst_helper(tree):
		if tree and len(k_largest_elements) < k:
			find_k_largest_in_bst_helper(tree.right)
			if len(k_largest_elements) < k:
				k_largest_elements.append(tree.data)
				find_k_largest_in_bst_helper(tree.left)
	
	k_largest_elements = []
	find_k_largest_in_bst_helper(tree)
	return k_largest_elements
