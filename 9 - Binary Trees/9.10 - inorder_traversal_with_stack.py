"""
Implement inorder traversal for binary trees without using recursion

Inorder DFS with recursion:

def inorder_traversal(tree):
	if not tree:
		return

	inorder_traversal(tree.left)
	print(tree.data)
	inorder_traversal(tree.right)

"""
# class BinaryTreeNode:
# 	def __init__(self, data=0, parent=None, left=None, right=None):
# 		self.data = data
# 		self.parent = parent
# 		self.left = left
# 		self.right = right


# def build_binary_tree(values, children):
# 	nodes = [BinaryTreeNode(val) for val in values]
# 	for i in range(len(children)):
# 		if children[i][0] != None:
# 			nodes[i].left = nodes[children[i][0]]
# 			nodes[children[i][0]].parent = nodes[i]
# 		if children[i][1] != None:
# 			nodes[i].right = nodes[children[i][1]]
# 			nodes[children[i][1]].parent = nodes[i]
# 	return nodes[0]


def inorder_traversal(tree):
	"""
	When coming down from parent node, always try to go left,
	if no left child, append the node.data to result and go
	right or parent.

	If coming from a left child node, append the node.data
	to result and try to go right or parent.

	If coming from a right child node, go parent.
	"""
	prev, results = None, []
	while tree:
		if prev is tree.parent:
			if tree.left:
				next = tree.left
			else:
				results.append(tree.data)
				next = tree.right or tree.parent
		elif prev is tree.left:
			results.append(tree.data)
			next = tree.right or tree.parent
		else:
			next = tree.parent

		prev, tree = tree, next
	return results


# values = range(9)
# children = [[1,2],[3,4],[5,6],[7,8]]
# tree = build_binary_tree(values, children)
# print(inorder_traversal(tree))
