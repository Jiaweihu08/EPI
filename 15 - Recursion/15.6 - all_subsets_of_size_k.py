"""
Given two integers n and k, with n >= k. Return all possible subsets
from [1,2,...,n-1] of size k.

Solution:
	For a given number in the range [1,2,...n-1], say 1, there are
	two possibilities - either a subset does not contain 1, or it
	does contain 1.
	
	In the first case, return all subsets of size k from [2,...,n-1].
	And in the second case, we return all subsets of size k - 1 from
	[2,...,n-1] and add 1 to each of them.
"""
def combinations(n, k):
	def directed_combinations(offset, subset_len):
		if len(A[offset:]) == subset_len:
			return [A[offset:]]

		elif subset_len == 1:
			return [[num] for num in A[offset:]]

		return ([[A[offset]] + sub for sub in
					directed_combinations(offset + 1, subset_len - 1)]
					+ directed_combinations(offset + 1, subset_len))
	
	A = list(range(1, n + 1))
	return directed_combinations(0, k)

print(combinations(6, 3))