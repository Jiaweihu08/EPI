"""
Given a cyclically sorted array, find the index of its smallest element
e.g. [4,5,6,7,8,1,2,3] --> idx = 5

Notice that, for any m, if A[m] > A[n - 1], then the smallest entry must
be in A[m + 1:n - 1]. Conversely, if A[m] < A[n - 1], then the smallest
entry is must certainly in A[l:m + 1]
"""
def search_smallest(A):
	left, right = 0, len(A) - 1
	while left < right:
		mid = (left + right) // 2
		if A[mid] > A[right]:
			left = mid + 1
		else:
			right = mid
	return left


A = [0,0,0,0,-1]
print(search_cyclically_sorted(A))


