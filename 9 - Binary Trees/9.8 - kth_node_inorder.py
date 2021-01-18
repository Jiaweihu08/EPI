"""
Given a binary tree and an integer k, find the kth node
when traversing the tree in an inorder fashion.
"""
def find_kth_node_binary_tree(tree, k):
	while tree:
		left_size = tree.left.size if tree.left else 0
		if left_size + 1 < k:
			k -= left_size + 1
			tree = tree.right
		elif left_size == k - 1:
			return tree
		else:
			tree = tree.left
	return None

	