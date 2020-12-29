"""
Given a sorted 2D array, return whether a given element is contained
within the array
"""
def search_in_2d_array_binary_search(A, x):
	"""
	Perform binary search on each row
	O(nlog(m)); n = num rows, m = num cols
	"""
	def binary_search(row, x):
		left, right = 0, len(row) - 1
		while left <= right:
			mid = (left + right) // 2
			if row[mid] == x:
				return True
			elif row[mid] < x:
				left = mid + 1
			else:
				right = mid + 1
		return False

	for row in A:
		if binary_search(row, x):
			return True
	return False


def search_in_2d_array(A, x):
	"""
	O(n + m) time complexity
	"""
	row, col = 0, len(A[0]) - 1
	while row < len(A) and col >= 0:
		if A[row][col] == x:
			return True
		if A[row][col] < x:
			row += 1
		else:
			col -= 1
	return False


A = [[-1,2, 4, 4, 6],
	 [1, 5, 5, 9,21],
	 [3, 6, 6, 9,22],
	 [3, 6, 8,10,24],
	 [6, 8, 9,12,25],
	 [8,10,12,13,40]]
k = 8
print(search_in_2d_array(A, k))
