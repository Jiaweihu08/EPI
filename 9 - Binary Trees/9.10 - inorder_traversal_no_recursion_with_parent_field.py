"""
Implement inorder traversal for binary trees without using recursion.

Hint: Analize cases depending on what the previous node is.
"""
def inorder_traversal(tree):
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

