"""
Reconstruct the binary tree from its preorder traversal data
with markers
"""
class BinaryTreeNode:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def binary_tree_from_preorder_with_markers(preorder):
	def binary_tree_from_preorder_with_markers_helper(idx):
		if idx >= len(preorder) or preorder[idx] == None:
			return None, idx

		root = BinaryTreeNode(preorder[idx])
		left_node, idx = binary_tree_from_preorder_with_markers_helper(idx + 1)
		root.left = left_node

		right_node, idx = binary_tree_from_preorder_with_markers_helper(idx + 1)
		root.right = right_node

		return root, idx

	return binary_tree_from_preorder_with_markers_helper(0)[0]


def reconstruct_preorder(preorder):
	def reconstruct_preorder_helper(preorder_iter):
		subtree_key = next(preorder_iter, 'stop')
		if subtree_key in (None, 'stop'):
			return None

		left_subtree = reconstruct_preorder_helper(preorder_iter)
		right_subtree = reconstruct_preorder_helper(preorder_iter)
		return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
	return reconstruct_preorder_helper(iter(preorder))


def preorder_traversal(tree):
	print(tree.data if tree else None)
	if not tree:
		return

	preorder_traversal(tree.left)
	preorder_traversal(tree.right)


preorder = ['H','B','F',None,None,'E','A',None,None,None,'C',None,'D',None,'G','I',None,None]
tree = reconstruct_preorder(preorder)
preorder_traversal(tree)

