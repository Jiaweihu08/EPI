"""
Given a bst and two nodes from the tree, return their lca
"""
import collections


Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))


def lca(tree, node1, node2):
	"""
	Compute for each node the number of target nodes it has
	as descendents
	"""
	def lca_helper(tree, node1, node2):
		if tree is None:
			return Status(0, None)

		left_result = lca_helper(tree.left, node1, node2)
		if left_result.num_target_nodes == 2:
			return left_result

		right_result = lca_helper(tree.right, node1, node2)
		if right_result.num_target_nodes == 2:
			return right_result

		num_target_nodes = (
			left_result.num_target_nodes +
			right_result.num_target_nodes +
			(node1, node2).count(tree)
		)
		return Status(num_target_nodes,
			tree if num_target_nodes == 2 else None)

	return lca_helper(tree, node1, node2).ancestor


def lca_for_bst(tree, s, b):
	"""
	Exploit the fact that BSTs are sorted
	Assuming that s.data < b.data

	O(h) time complexity
	"""
	def lca_helper(tree, s, b):
		if tree.data > b.data:
			return lca_helper(tree.left, s, b)
		elif tree.data < s.data:
			return lca_helper(tree.right, s, b)
		else:
			return tree
	return lca_helper(tree, s, b)


def lca_for_bst(tree, s, b):
	while tree.data < s.data or tree.data > b.data:
		while tree.data < s.data:
			tree = tree.right
		while tree.data > b.data:
			tree = tree.left
	return tree

