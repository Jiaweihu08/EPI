"""
Given a bst and two nodes from the tree, return their lca
"""
def lca_for_bst(tree, s, b):
	while tree.data < s.data or tree.data > b.data:
		while tree.data < s.data:
			tree = tree.right
		while tree.data > b.data:
			tree = tree.left
	return tree

