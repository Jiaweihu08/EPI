"""
Given a sequence of node keys visited in inorder traversal and another sequence
of node keys visited in preorder traversal, reconstruct the BST.
"""
def BinaryTreeNode:
	def __init__(self, data=0, left=None, right=None):
		self.data, self.left, self.right = data, left, right


# def binary_tree_from_preorder_inorder(preorder, inorder):
# 	"""
# 	Review reconstructing a Binary Tree from preorder plus inorder traversal
# 	data.
# 	"""
# 	node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
# 	def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
# 													inorder_start, inorder_end):
# 		if preorder_start >= preorder_end or inorder_start >= inorder_end:
# 			return None
# 		root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
# 		left_tree_size = root_inorder_idx - inorder_start
# 		return TreeNode(preorder[preorder_start],
# 			binary_tree_from_preorder_inorder_helper(
# 				preorder_start + 1, preorder_start + 1 + left_tree_size,
# 				inorder_start, root_inorder_idx),
# 			binary_tree_from_preorder_inorder_helper(
# 				preorder_start + 1 + left_tree_size, preoder_end,
# 				root_inorder_idx + 1, inorder_end))
# 	return binary_tree_from_preorder_inorder_helper(
# 		preorder_start = 0,
# 		preorder_end = len(preorder),
# 		inorder_start = 0,
# 		inorder_end = len(inorder))


def bst_from_inorder(inorder):
	print('Not possible to reconstruct a bst only from\
		inorder traversal data')
	return None


def bst_from_preorder(preorder_sequence):
	def bst_from_preorder_helper(lower_bound, upper_bound):
		if root_idx[0] == len(preorder_sequence):
			return None
		root_key = preorder_sequence[root_idx[0]]
		if not lower_bound <= root <= upper_bound:
			return None
		root_idx[0] += 1
		left_subtree = bst_from_preorder_helper(
			lower_bound, node_key)
		right_subtree = bst_from_preorder_helper(
			node_key, upper_bound)
		return TreeNode(node_key, left_subtree, right_subtree)

	root_idx = [0]
	return bst_from_preorder_helper(float('-inf'), float('inf'))


def bst_from_postorder(postorder):
	def bst_from_postorder_helper(lower_bound, upper_bound):
		if root_idx[0] == -1:
			return None
		root = postorder[root_idx[0]]
		if not lower_bound <= root <= upper_bound:
			return None
		root_idx[0] -= 1
		right_subtree = bst_from_postorder_helper(root, upper_bound)
		left_subtree = bst_from_postorder_helper(lower_bound, root)
		return TreeNode(root, left_subtree, right_subtree)
	root_idx = [len(postorder) - 1]
	return bst_from_postorder_helper(float('-inf'), float('inf'))


