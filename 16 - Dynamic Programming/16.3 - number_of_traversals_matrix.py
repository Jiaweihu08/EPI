import functools


def number_of_traversals_matrix(n, m):
	@functools.lru_cache(None)
	def number_of_traversals_helper(i, j):
		if i == 0 or j == 0:
			return 1
			
		return (number_of_traversals_helper(i - 1, j) +
				number_of_traversals_helper(i, j - 1))

	return number_of_traversals_helper(n - 1, m - 1)


print(number_of_traversals_matrix(5, 5))