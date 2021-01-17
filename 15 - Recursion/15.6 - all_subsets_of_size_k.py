"""
Given two integers n and k, with n >= k. Return all possible subsets
from [1,2,...,n - 1] of size k.
"""
def combinations_with_bc(n, k):
	"""
	The number of all possible subsets of size k from the defined range
	is also known as binomial coefficient of (n, k), bc(n, k). A propperty
	of binomial coefficients worth knowing is that bs (n, k) can be
	obtained by computing tthe union between the bc(n - 1, k) and
	bc(n - 1, k - 1).

	For subsets of size k from range [1,2,...n - 1] and a given element
	from the range, say 1, there are two possibilities - either a subset
	does not contain 1, or it does contain it.

	In the first case, find all subsets of size k from [2,...,n - 1].
	In the second case, we find all subsets of size k - 1 from
	[2,...,n - 1] and add 1 to each of them. In each case we reduce the
	size of the range. The union of these two are the solution we looking
	for.
	"""
	def combinations_with_bc_helper(offset, subset_size):
		if len(A[offset:]) == subset_size:
			return [A[offset:]]

		elif subset_size == 1:
			return [[num] for num in A[offset:]]

		return ([[A[offset]] + sub for sub in
					combinations_with_bc_helper(offset + 1, subset_size - 1)]
					+ combinations_with_bc_helper(offset + 1, subset_size))
	
	A = list(range(1, n + 1))
	return combinations_with_bc_helper(0, k)


def combinations(n, k):
	def directed_combinations(offset, partial_combination):
		if len(partial_combination) == k:
			result.append(partial_combination)
			return

		num_remaining = k - len(partial_combination)
		for i in range(offset, n - num_remaining + 2):
			directed_combinations(i + 1, partial_combination + [i])

		# i = offset
		# while i <= n and num_remaining <= n - i + 1:
		# 	directed_combinations(i + 1, partial_combination + [i])
		# 	i += 1

	result = []
	directed_combinations(1, [])
	return result


print(combinations(7, 3))