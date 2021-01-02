"""
Given a sorted array of integers with repeated elements and a element k,
return the position at which the first occurrences of k is found
"""
def search_first_of_k_naive(A, k):
	"""
	O(n) time complexity if all entries are k
	"""
	l, r = 0, len(A) - 1
	while l <= r:
		m = (l + r) // 2
		if A[m] == k:
			while m > 0 and A[m - 1] == k:
				m -= 1
			return m
		elif A[m] < k:
			l = m + 1
		else:
			r = m - 1
	return -1


def search_first_of_k(A, k):
	"""
	The naive implementation stops the binary search
	as soon as an occurrence of k is found, then it
	proceeds to go left until an entry that is not k
	is found

	In order to keep exploting the benefits of binary
	search, whenever k is encountered we store that
	index as the result and define it as the right
	limit so we can keep using binary search
	"""
	l, r, result = 0, len(A) - 1, -1
	while l <= r:
		m = (l + r) // 2
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
print(search_first_of_k_naive(A, k))

