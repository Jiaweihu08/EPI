"""
Check if a given binary tree is symmetric. If we draw a vertical line
through the root node, is the left tree the mirror image of the right tree?
"""
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


def is_symmetric(tree):
	def check_symmetric(subtree_0, subtree_1):
		if not subtree_0 and not subtree_1:
			return True
		elif subtree_1 and subtree_1:
			return (subtree_0.data == subtree_1.data
				and check_symmetric(subtree_0.left, subtree_1.right)
				and check_symmetric(subtree_0.right, subtree_1.left))
		return False
	return not tree or check_symmetric(tree.left, tree.right)


values = [0,1,1,2,3,3,2,4,5,6,7,7,6,5,4]
children = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]
tree = build_binary_tree(values, children)
print(is_symmetric(tree))
