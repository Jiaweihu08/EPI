def binary_tree_exterior(tree):
	def left_boundary(subtree):
		if not subtree or (not subtree.left and not subtree.right):
			return
		exterior.append(subtree)
		if subtree.left:
			left_boundary(subtree.left)
		else:
			left_boundary(subtree.right)

	def right_boundary(subtree):
		if not subtree or (not subtree.left and not subtree.right):
			return
		if subtree.right:
			right_boundary(subtree.right)
		else:
			right_boundary(subtree.left)
		exterior.append(subtree)

	def leaves(subtree):
		if not subtree:
			return
		if not subtree.left and not subtree.right:
			exterior.append(subtree)
			return
		leaves(subtree.left)
		leaves(subtree.right)

	if not tree:
		return []
	
	exterior = [tree]
	left_boundary(tree.left)
	leaves(tree.left)
	leaves(tree.right)
	right_boundary(tree.right)
	return exterior