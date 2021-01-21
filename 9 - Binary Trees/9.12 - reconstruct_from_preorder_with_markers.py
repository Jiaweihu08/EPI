"""
Reconstruct the binary tree from its preorder traversal data with markers.
"""
def binary_tree_from_preorder_with_markers(preorder):
	def binary_tree_from_preorder_helper():
		if index[0] >= len(preorder) or preorder[index[0]] is None:
			index[0] += 1
			return None
		node_data = preorder[index[0]]
		index[0] += 1
		return BinaryTreeNode(
			node_data,
			binary_tree_from_preorder_helper(),
			binary_tree_from_preorder_helper())
	index = [0]
	return binary_tree_from_preorder_helper()


def reconstruct_preorder(preorder):
	"""
	A more elegant solution using iterator.
	"""
	def reconstruct_preorder_helper(preorder_iter):
		subtree_key = next(preorder_iter, None)
		if subtree_key is None:
			return None
		return BinaryTreeNode(
			subtree_key,
			reconstruct_preorder_helper(preorder_iter),
			reconstruct_preorder_helper(preorder_iter))
	return reconstruct_preorder_helper(iter(preorder))
