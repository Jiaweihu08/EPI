"""
Given a binary tree, design an algorithm to find all leaves
in the tree.
"""
def tree_leaves(tree):
	def find_subtree_leaf(tree):
		if not tree:
			return
		if not tree.left and not tree.right:
			result.append(tree)
			return
		find_subtree_leaf(tree.left)
		find_subtree_leaf(tree.right)

	result = []
	find_subtree_leaf(tree)
	return result


def create_list_of_leaves(tree):
    if not tree:
        return []

    if not tree.left and not tree.right:
        return [tree]

    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)
