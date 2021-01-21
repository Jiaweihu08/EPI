"""
Given a binary tree with integer node data and a integer number.
Write a program to determine if there exists a path sum from root
to any leaf that's equal to the given integer number.
"""
def has_path_sum_increment(tree, target_sum):
	def has_path_sum_helper(tree, curr_sum):
		if not tree:
			return False

		curr_sum += tree.data
		if not tree.left and not tree.right:
			return curr_sum == target_sum

		return (has_path_sum_helper(tree.left, curr_sum)
				or has_path_sum_helper(tree.right, curr_sum))
	return has_path_sum_helper(tree, 0)


def has_path_sum(tree, remaining_weight):
	if not tree:
		return False

	if not tree.left and not tree.right:
		return remaining_weight == tree.data

	return (has_path_sum(tree.left, remaining_weight - tree.data)
		or remaining_weight(tree.right, remaining_weight - tree.data))

	