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


print(levenshtein_distance('saturday', 'sundays'))