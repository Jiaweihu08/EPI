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
class BinaryTreeNode:
	def __init__(self, data=0, parent=None, left=None, right=None):
		self.data = data
		self.parent = parent
		self.left = left
		self.right = right


def build_binary_tree(values, children):
	nodes = [BinaryTreeNode(val) for val in values]
	for i in range(len(children)):
		if children[i][0] != None:
			nodes[i].left = nodes[children[i][0]]
			nodes[children[i][0]].parent = nodes[i]
		if children[i][1] != None:
			nodes[i].right = nodes[children[i][1]]
			nodes[children[i][1]].parent = nodes[i]
	return nodes[0]


def inorder_traversal(tree):
	prev, results = None, []
	while tree:
		if prev is tree.parent:
			# coming down from a parent node
			if tree.left:
				# keep doing left
				next = tree.left
			else:
				# go right or up
				results.append(tree.data)
				next = tree.right or tree.parent

		elif prev is tree.left:
			# coming up from the left child
			results.append(tree.data)
			# go right or up
			next = tree.right or tree.parent
		
		else:
			# coming from the right child
			# go up
			next = tree.parent

		prev, tree = tree, next
	return results


values = range(9)
children = [[1,2],[3,4],[5,6],[7,8]]
tree = build_binary_tree(values, children)
print(inorder_traversal(tree))
