"""
Given a cyclically sorted array, find the index of its smallest element
e.g. [4,5,6,7,8,1,2,3] --> idx = 5
"""
def search_cyclically_sorted(A):
	l, r = 0, len(A) - 1
	while l <= r:
		m = l + (r - l) // 2
		if A[m] < A[m - 1]:
			return m
		elif A[m] < A[0]:
			r = m - 1
		else:
			l = m + 1


def search_smallest(A):
	left, right = 0, len(A) - 1
	while left <= right:
		mid = (left + right) // 2
		if A[mid] < A[right]:
			left = mid + 1
		else:
			right = mid
	return mid


A = [0,0,0,0,-1]
print(search_cyclically_sorted(A))


