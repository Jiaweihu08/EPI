"""
Given the inorder traversal data and the preorder traversal data
of a binary tree, reconstruct the tree.

The first node in the preorder traversal is always the root of the
current tree. If we locate this node in the inorder traversal data,
all nodes on its right side are the nodes from its left subtree,
and all nodes on the right side are the nodes from its right subtree.
"""
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

