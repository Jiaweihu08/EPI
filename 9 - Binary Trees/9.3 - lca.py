"""
Given a binary tree, and two nodes, find the LCA of these two nodes
in the tree. Nodes don't have a parent pointer.
"""
import collections


def lca(tree, node0, node1):
	"""
	O(n) time complexity
	O(h) space complexity
	"""
	Status = collections.namedtuple('Status',['num_target_nodes', 'ancestor'])
	def lca_helper(tree, node0, node1):
		if not tree:
			return Status(num_target_nodes=0, ancestor=None)

		left_result = lca_helper(tree.left, node0, node1)
		if left_result.num_target_nodes == 2:
			return left_result

		right_result = lca_helper(tree.right, node0, node1)
		if right_result.num_target_nodes == 2:
			return right_result

		num_target_nodes = (left_result.num_target_nodes +
							right_result.num_target_nodes +
							(node0, node1).count(tree))
		return Status(num_target_nodes,
					tree if num_target_nodes == 2 else None)

	return lca_helper(tree, node0, node1).ancestor