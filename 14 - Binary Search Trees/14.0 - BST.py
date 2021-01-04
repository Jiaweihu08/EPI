def search_bst(tree, data):
	return (tree if not tree or tree.data == data else
		search_bst(tree.left) if data < tree.data else
		search_bst(tree.right))