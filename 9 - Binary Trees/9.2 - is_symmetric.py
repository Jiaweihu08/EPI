"""
Check if a given binary tree is symmetric. If we draw a vertical line
through the root node, is the left tree the mirror image of the right
tree?
"""
def is_symmetric(tree):
	def check_symmetric(subtree_0, subtree_1):
		if not subtree_0 and not subtree_1:
			return True
		elif subtree_1 and subtree_1:
			return (subtree_0.data == subtree_1.data
				and check_symmetric(subtree_0.left, subtree_1.right)
				and check_symmetric(subtree_0.right, subtree_1.left))
		return False
	return not tree or check_symmetric(tree.left, tree.right)
