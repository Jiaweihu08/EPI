"""
Given a binary tree whose node data are either 1 or 0.
Design an algorithm to compute the sum of all binary numbers
represented by paths from root the leafs.
"""
import functools
import string


def sum_root_to_leaf_nlogn(root):
	"""
	All nodes are visited, and at each leaf node
	the binary number constructed along the path
	is converted to a decimal number.

	The time complexity for the conversion is
	proportional to the length of the path, in the
	worst case its the height of the tree, log(n)

	Time complexity O(nlog(n))
	Space complexity O(n), since we visit all nodes
	and at each node there's a recursion call.
	"""
	def binary_to_decimal(binary_in_string):
		return functools.reduce(
			lambda c, i: c * 2 + string.digits.index(i),
			binary_in_string, 0)

	def add_next(node, partial_sum):
		if not node:
			return 0

		partial_sum += str(node.data)
		if not node.left and not node.right:
			return binary_to_decimal(partial_sum)

		return (add_next(node.left, partial_sum) +
				add_next(node.right, partial_sum))

	return add_next(root, '')


def sum_root_to_leaf(root):
	def sum_root_to_leaf_helper(tree, partial_sum):
		if not tree:
			return 0
		
		partial_sum = partial_sum * 2 + tree.data
		if not tree.left and not tree.right:
			return partial_sum
		
		return (sum_root_to_leaf_helper(tree.left, partial_sum) +
				sum_root_to_leaf_helper(tree.right, partial_sum))
	
	return sum_root_to_leaf_helper(tree, 0)

