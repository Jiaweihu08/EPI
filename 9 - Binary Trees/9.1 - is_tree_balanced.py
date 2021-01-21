"""
Given a binary tree, check whether the tree is balanced.
A binary tree is said to be balanced if for each node the difference between
the height of its left and right subtree is at most one.
"""
import collections


def is_tree_balanced(tree):
	BalancedStatusWithHeight = collections.namedtuple(
		'BalancedStatusWithHeight',
		['is_balanced', 'height'])
	def check_balanced(tree):
		if not tree:
			return BalancedStatusWithHeight(True, -1)
		
		left_result = check_balanced(tree.left)
		if not left_result.is_balanced:
			return left_result

		right_result = check_balanced(tree.right)
		if not right_result.is_balanced:
			return right_result

		is_balanced = abs(left_result.height - right_result.height) <= 1
		height = max(left_result.height, right_result.height) + 1
		return BalancedStatusWithHeight(is_balanced, height)

	return check_balanced(tree).is_balanced

