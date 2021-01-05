"""
Given a binary tree, check if it satisfies the property of BST
"""
import collections


def is_binary_tree(tree):
	"""
	Check if each node's data are in their valid ranges using DFS
	Time complexity O(n)
	Space complexity O(h), h is the height of the tree
	"""
	def is_valid_key(tree,
		left_limit=float('-inf'),
		right_limit=float('inf')):
		if not tree:
			return True
		if not left_limit <= tree.data <= right_limit:
			return False
		return (is_valid_key(tree.left, left_limit, tree.data)
				and is_valid_key(tree.right, tree.data, right_limit))
	return is_valid_key(tree)


def is_binary_tree_inorder_traversal(tree):
	"""
	Exploit the fact that an inorder traversal renders data in
	sorted order for BST

	Use inorder traversal to check whether the current key is
	smaller the the previous key
	O(n) time complexity, O(h) space complexity
	"""
	def inorder_traversal(tree, prev=float('-inf')):
		if not tree:
			return True, prev

		valid_left_subtree, prev = inorder_traversal(tree.left, prev)
		if not valid_left_subtree or prev > tree.data:
			return False, prev

		return inorder_traversal(tree.right, tree.data)
	return inorder_traversal(tree)[0]


def is_binary_tree(tree):
	"""
	The previous methods checks nodes in DFS fashion, if the node that
	violates BST property is close to the root but not on the left
	subtree, the space complexity is still O(n)

	Check the tree nodes with BFS to improve efficiency
	"""
	QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
	bfs_queue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])

	while bfs_queue:
		front = bfs_queue.popleft()
		if front.node:
			if not front.lower <= front.node.data <= front.upper:
				return False
			bfs_queue.extend((
				QueueEntry(front.node.left, front.lower, front.node.data),
				QueueEntry(front.node.right, front.node.data, front.upper)))
	return True


# Tested with EPIJudge
