"""
Different inorder traversal implementations
"""
def inorder_recursive(tree):
	def inorder_dfs(tree):
		if not tree:
			return
		inorder_dfs(tree.left)
		result.append(tree.data)
		inorder_dfs(tree.right)

	result = []
	inorder_dfs(tree)
	return result


def inorder_iterative(tree):
	result = []
	in_process = [(tree, False)]
	while in_process:
		node, left_subtree_processed = in_process.pop()
		if node:
			if left_subtree_processed:
				result.append(node.data)
			else:
				in_process.append((node.left, False))
				in_process.append((node, True))
				in_process.append((node.right, False))
	return result


def inorder_with_parent_field(tree):
	prev, result = None, []
	while tree:
		if prev is tree.parent:
			if tree.left:
				next = tree.left:
			else:
				result.append(tree.data)
				next = tree.right or tree.parent
		elif prev is tree.left:
			result.append(tree.data)
			next = tree.right or tree.parent
		else:
			next = tree.parent
		prev, tree = tree, next
	return result

