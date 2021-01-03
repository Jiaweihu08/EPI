"""
Given two sorted arrays, extend the firsrt array with the entries
of the second one so the result is also sorted. Assume that the
first array has enough empty entries at its end to store all entries
from the second one
"""
def merge_two_sorted_arrays_n_space(A, B):
	i, j, result = 0, 0, []
	while i < len(A) and j < B[j]:
		if A[i] == B[j]:
			result.extend([A[i], B[j]])
			i, j = i + 1, j + 1
		elif A[i] > B[j]:
			result.append(B[j])
			j += 1
		else:
			result.append(A[i])
			i += 1
	result.extend(A[i:] or B[j:])
	return result


def merge_two_sorted_arrays(A, m, B, n):
	"""
	Start filling A from the back with the largest remaining
	value from the rest of A and B
	"""
	i, j, write_idx = m - 1, n - 1, m + n - 1
	while i >= 0 and j >= 0:
		if A[i] > B[j]:
			A[write_idx] = A[i]
			i -= 1
		else:
			A[write_idx] = B[j]
			j -= 1
		write_idx -= 1
	while j >= 0:
		A[write_idx] = B[j]
		j, write_idx = j - 1, write_idx - 1
	return A



A = [3,13,17,0,0,0,0]
B = [3,7,11,19]
# print(merge_two_sorted_arrays_n_space(A, B))
print(merge_two_sorted_arrays(A, 3, B, 4))

