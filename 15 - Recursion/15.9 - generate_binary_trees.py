"""
Generate all possible n node binary trees

The variation on each n node binary tree is that it can have an i
node left subtree and a (n - i - 1) node right subtree, for all
possible values of i. Same is applied to each subtree.

For each recursion call, we generate all possible subtrees with
different sizes and variations, then we combine these subtrees as
either left or right child of the root node, taking into account
the fact that their size shoud sum to n - 1.
"""
# class BinaryTreeNode:
# 	def __init__(self, key, left=None, right=None):
# 		self.key = key
# 		self.left = left
# 		self.right = right


def generate_all_binary_trees(num_nodes):
	if num_nodes == 0:
		return [None]

	result = []
	size_to_subtree = {i: generate_all_binary_trees(i) for i in range(num_nodes)}

	for left_subtree_size in range((num_nodes - 1) // 2 + 1):
		right_subtree_size = num_nodes - 1 - left_subtree_size
		for left_subtree in size_to_subtree[left_subtree_size]:
			for right_subtree in size_to_subtree[right_subtree_size]:
				result.append(BinaryTreeNode(0, left_subtree, right_subtree))
				if left_subtree_size != right_subtree_size:
					result.append(BinaryTreeNode(0, right_subtree, left_subtree))
	return result

