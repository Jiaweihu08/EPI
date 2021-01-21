"""
Compute the LCA of two nodes in a binary tree, assuming that
nodes have a parent field.
"""
def lca_naive(tree, node0, node1):
	"""
	O(h) time and space complexity
	h is the height of the tree
	"""
	ancestors = set()
	while node0:
		ancestors.add(node0)
		node0 = node0.parent
	while node1 not in ancestors:
		node1 = node1.parent
	return node1


def lca(tree, node0, node1):
	"""
	O(h) time complexity
	O(1) space complexity

	h is the height of the tree
	"""
	def get_depth(node):
		depth = 0
		while node.parent:
			depth += 1
			node = node.parent
		return depth

	depth0, depth1 = map(get_depth, (node0, node1))
	if depth1 > depth0:
		node0, node1 = node1, node0

	depth_diff = abs(depth1 - depth0)
	while depth_diff:
		node0 = node0.parent
		depth_diff -= 1

	while node0 is not node1:
		node0, node1 = node0.parent, node1.parent
	return node0

