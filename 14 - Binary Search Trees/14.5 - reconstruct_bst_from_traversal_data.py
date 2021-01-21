"""
Given a sequence of node keys visited in inorder traversal and another sequence
of node keys visited in preorder traversal, reconstruct the BST.
"""
def bst_from_inorder(inorder):
	print('Not possible to reconstruct a bst only from\
		inorder traversal data')
	return None


def bst_from_preorder(preorder_sequence):
	def bst_from_preorder_helper(lower_bound, upper_bound):
		if root_idx[0] == len(preorder_sequence):
			return None
		root_key = preorder_sequence[root_idx[0]]
		if not lower_bound <= root_key <= upper_bound:
			return None
		root_idx[0] += 1
		return BstNode(root_key,
			bst_from_preorder_helper(lower_bound, root_key),
			bst_from_preorder_helper(root_key, upper_bound))

	root_idx = [0]
	return bst_from_preorder_helper(float('-inf'), float('inf'))


def bst_from_preorder(preorder_sequence):
	if not preorder_sequence:
		return None

	transition_point = next(
		(i for i, a in preorder_sequence if a > preorder_sequence[0]),
		len(preorder_sequence))
	return BstNode(preorder_sequence[0],
		bst_from_preorder(preorder_sequence[:transition_point]),
		bst_from_preorder(preorder_sequence[transition_point:]))


def bst_from_postorder(postorder):
	def bst_from_postorder_helper(lower_bound, upper_bound):
		if root_idx[0] == -1:
			return None
		root_key = postorder[root_idx[0]]
		if not lower_bound <= root_key <= upper_bound:
			return None
		root_idx[0] -= 1
		return BstNode(root_key,
			bst_from_postorder_helper(root_key, upper_bound),
			bst_from_postorder_helper(lower_bound, root_key))
	root_idx = [len(postorder) - 1]
	return bst_from_postorder_helper(float('-inf'), float('inf'))

