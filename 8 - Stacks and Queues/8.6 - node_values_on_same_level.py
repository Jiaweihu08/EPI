"""
Given the root node of a binary tree, return a list
of list consisting of node values on the same level
"""
# import collections


class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def build_tree(values, children):
	tree_nodes = [Node(data) for data in values]
	for i in range(len(children)):
		node = tree_nodes[i]
		if children[i][0] != -1:
			node.left = tree_nodes[children[i][0]]
		if children[i][1] != -1:
			node.right = tree_nodes[children[i][1]]
	return tree_nodes[0]


# def binary_tree_depth_order(tree):
# 	all_vals, level_vals = [], []
# 	if not tree:
# 		return all_vals
# 	current_depth, next_depth = collections.deque(), collections.deque()
# 	current_depth.append(tree)
# 	while current_depth:
# 		node = current_depth.popleft()
# 		level_vals.append(node.key)
# 		if node.left:
# 			next_depth.append(node.left)
# 		if node.right:
# 			next_depth.append(node.right)
# 		if not current_depth:
# 			current_depth, next_depth = next_depth, collections.deque()
# 			all_vals.append(level_vals)
# 			level_vals = []
# 	return all_vals


def binary_tree_depth_order(tree):
	result = []
	if not tree:
		return result

	current_depth_nodes =[tree]
	while current_depth_nodes:
		result.append([node.data for node in current_depth_nodes])
		current_depth_nodes = [
			child for curr in current_depth_nodes
			for child in (curr.left, curr.right) if child
		]
	return result



values = list(range(1, 14))
children = [[1,2],[3,4],[5,6],[7,-1],[8,-1],[-1,9],[10,11],[-1,-1],[12,-1]]
root = build_tree(values, children)
print(binary_tree_depth_order(root))


