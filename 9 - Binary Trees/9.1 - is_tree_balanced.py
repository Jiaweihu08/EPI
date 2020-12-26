"""
Given a binary tree, check whether the tree is balanced
A binary tree is said to be balanced if for each node
the difference between the height of its left subtree
and its right subtree is at most one
"""
import collections


class BinaryTreeNode:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def build_binary_tree(values, children):
	nodes = [BinaryTreeNode(val) for val in values]
	for i in range(len(children)):
		if children[i][0] != None:
			nodes[i].left = nodes[children[i][0]]
		if children[i][1] != None:
			nodes[i].right = nodes[children[i][1]]
	return nodes[0]


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



values = range(9)
children = [[1,2],[3,4],[None,None],[7,8]]
tree = build_binary_tree(values, children)

print(is_tree_balanced(tree))


