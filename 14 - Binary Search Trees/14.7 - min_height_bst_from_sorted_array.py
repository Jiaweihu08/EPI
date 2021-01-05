"""
Given an sorted array, return a bst with minimum height
"""
def BinaryTreeNode:
	def __init__(self, data=0, left=None, right=None):
		self.data, self.left, self.right = data, left, right


def build_min_height_bst_from_sorted_array(A):
	def build_min_height_bst_from_sorted_array_helper(start, end):
		if start >= end:
			return None

		mid = (start + end) // 2
		return TreeNode(A[mid],
				build_min_height_bst_from_sorted_array_helper(start, mid),
				build_min_height_bst_from_sorted_array_helper(mid + 1, end))
	return build_min_height_bst_from_sorted_array_helper(0, len(A))

