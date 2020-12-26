"""
Given the inorder traversal data and the preorder traversal data
of a binary tree, reconstruct the tree
"""
class BinaryTreeNode:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def binary_tree_from_preorder_inorder(preorder, inorder):
	node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

	def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
												inorder_start, inorder_end):
		if preorder_start >= preorder_end or inorder_start >= inorder_end:
			return None

		root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
		left_subtree_size = root_inorder_idx - inorder_start
		return BinaryTreeNode(
			preorder[preorder_start],
			binary_tree_from_preorder_inorder_helper(
				preorder_start + 1, preorder_start + 1 + left_subtree_size,
				inorder_start, root_inorder_idx),
			binary_tree_from_preorder_inorder_helper(
				preorder_start + 1 + left_subtree_size, preorder_end,
				root_inorder_idx + 1, inorder_end))

	return binary_tree_from_preorder_inorder_helper(
			0, len(preorder), 0, len(inorder))


def tree_traversal(tree, traversal='pre'):
	if not tree:
		return

	if traversal == 'pre':
		print(tree.data, end=' ')	
	tree_traversal(tree.left, traversal)

	if traversal == 'in':
		print(tree.data, end=' ')
	tree_traversal(tree.right, traversal)

	if traversal == 'post':
		print(tree.data, end=' ')


inorder = ['E','B','F','G','H','L','C','A','I','J']
preorder = ['H','B','E','F','G','C','L','I','A','J']

tree = binary_tree_from_preorder_inorder(preorder, inorder)
tree_traversal(tree, 'pre')

