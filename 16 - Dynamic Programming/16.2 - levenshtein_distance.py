"""
Given two strings A and B, compute the minimum number of edits required
to convert A into B. Allowed edits are substitution, insertion, and
deletion.
"""
import functools


def levenshtein_distance(A, B):
	@functools.lru_cache(None)
	def compute_distance_between_prefixes(A_idx, B_idx):
		if A_idx < 0:
			return B_idx + 1
		elif B_idx < 0:
			return A_idx + 1
		if A[A_idx] == B[B_idx]:
			return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)

		substitute_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
		add_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
		delete_last = compute_distance_between_prefixes(A_idx - 1, B_idx)

		return 1 + min(substitute_last, add_last, delete_last)

	return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)


def levenshtein_distance_minab_space(A, B):
	if len(B) > len(A):
		A, B = B, A
	dp = [i for i in range(len(B) + 1)]

	for i in range(len(A)):
		substitute_last = dp[0]
		dp[0] = i + 1
		for j in range(1, len(B) + 1):
			if A[i] == B[j - 1]:
				dp[j],  substitute_last = substitute_last, dp[j]
				continue
			next_sub = delete_last = dp[j]
			insert_last = dp[j - 1]
			dp[j] = 1 + min(substitute_last, insert_last, delete_last)
			substitute_last = next_sub
	return dp[-1]


print(levenshtein_distance_minab_space('Orchestra', 'Carthorse'))