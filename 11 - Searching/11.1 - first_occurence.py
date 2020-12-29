"""
Given a sorted array of integers with repeated elements and a element k,
return the position at which the first occurrences of k is found
"""
def search_first_of_k_naive(A, k):
	"""
	O(n) time complexity if all entries are k
	"""
	l, r = 0, len(A)
	while l < r:
		m = l + (r - l) // 2
		if A[m] == k:
			while m > 0 and A[m - 1] == k:
				m -= 1
			return m
		elif A[m] < k:
			l = m + 1
		else:
			r = m
	return -1


def search_first_of_k(A, k):
	l, r, result = 0, len(A) - 1, -1
	while l <= r:
		m = l + (r - l) // 2
		if A[m] == k:
			result = m
			r = m - 1
		elif A[m] < k:
			l = m + 1
		else:
			r = m - 1
	return result


A = [0,1,2,3,4,4,4,5,6]
k = 4
print(search_first_of_k(A, k))

