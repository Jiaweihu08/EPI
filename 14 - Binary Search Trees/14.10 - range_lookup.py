"""
Given a BST and an interval, return all keys from the tree that lie in
the interval
"""
import collections


Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst_naive(tree, interval):
	"""
	Traverse the tree in any DFS fashion and append the key to the 
	result if it lies in the interval

	O(n) time complexity
	"""
	def dfs(node):
		"""
		Perform inorder traversal, preorder and postorder would
		also work.

		Inorder traversal will return the results sorted.
		"""
		if not node:
			return
		dfs(node.left)
		if interval.left <= node.data <= interval.right:
			result.append(node.data)
		dfs(node.right)
	result = []
	dfs(tree)
	return result


def range_look_up_in_bst(tree, interval):
	"""
	The previous algorithm does not exploit the BST property - it works
	unchanged for an arbitrary binary tree.

	If a given node's key is smaller than the interval's left limit, its
	left subtree will only contain smaller values, and we only need to
	chekc its right subtree.

	Similarly, if a node's key is greater than the interval's right limit,
	we only check its left subtree.
	"""
	def range_lookup_in_bst_helper(tree):
		if not tree:
			return

		if interval.left <= tree.data <= interval.right:
			range_lookup_in_bst_helper(tree.left)
			result.append(tree.data)
			range_lookup_in_bst_helper(tree.right)
		elif tree.data < interval.left:
			range_lookup_in_bst_helper(tree.right)
		else:
			range_lookup_in_bst_helper(tree.left)
			
	result = []
	range_lookup_in_bst_helper(tree)
	return result


