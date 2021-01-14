"""
Given a nxm grid starting at the top-left corner. Compute the number of
distinct paths to get to the bottom-right corner if we're only allowed
to go right or down.
"""
import functools


def number_of_traversals_matrix(n, m):
	"""
	O(nm) space and time complexity
	"""
	@functools.lru_cache(None)
	def number_of_traversals_helper(i, j):
		if i == 0 or j == 0:
			return 1
		return (number_of_traversals_helper(i - 1, j) +
				number_of_traversals_helper(i, j - 1))
	return number_of_traversals_helper(n - 1, m - 1)


def number_of_traversals_matrix_minab_space(n, m):
	"""
	O(nm) time complexity
	O(min(a, b)) space complexity
	"""
	if m > n:
		n, m = m, n
	dp = [1] * m

	for i in range(1, n):
		for j in range(1, m):
			dp[j] += dp[j - 1]
	return dp[-1]


print(number_of_traversals_matrix_minab_space(5, 5))