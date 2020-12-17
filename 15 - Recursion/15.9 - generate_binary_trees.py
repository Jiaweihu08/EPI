class BinaryTreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.val)


def generate_all_binary_trees(n):
	if n == 1:
		return [BinaryTreeNode(n)]

	results = []
	sub_trees = {0: [None]}
	for i in range(1, n):
		sub_trees[i] = generate_all_binary_trees(i)

	for i in range((n - 1) // 2 + 1):
		for node_l in sub_trees[i]:
			for node_r in sub_trees[n-1-i]:
				results.append(BinaryTreeNode(n, node_l, node_r))
				if i != n-1-i:
					results.append(BinaryTreeNode(n, node_r, node_l))

	return results


def bfs(node):
	stack = [[node, 'root']]
	while stack:
		node, msg = stack.pop()
		print(node, msg)
		if node.right:
			stack.append([node.right, 'right'])
		if node.left:
			stack.append([node.left, 'left'])

for tree in generate_all_binary_trees(4):
	bfs(tree)
	print('-----')
