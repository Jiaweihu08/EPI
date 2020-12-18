"""
Given a partially assigned sudoku, return True if this
partial assignment is valid, False otherwise
"""
import math
import collections


def is_valid_sudoku(A):
	"""
	Using recursion and backtracking

	For each position i, j in A, check for duplicates in row i,
	col j, and the subgrid

	"""
	def checker_helper(i, j):
		if j == 9:
			j = 0
			i += 1
			if i == 9:
				return True

		if A[i][j] == 0:
			return checker_helper(i, j + 1)

		# check if the current assignment is valid
		# check current row i
		if A[i][j] in A[i][:j] + A[i][j + 1:]:
			return False

		# check current col j
		for row in A[:i] + A[i + 1:]:
			if row[j] == A[i][j]:
				return False

		# check current 3x3 grid
		y_min, y_max = 3 * (i // 3), 3 * (i // 3 + 1)
		x_min, x_max = 3 * (j // 3), 3 * (j // 3 + 1)
		for row_idx in range(y_min, y_max):
			for col_idx in range(x_min, x_max):
				if A[row_idx][col_idx] == A[i][j] and \
				(row_idx, col_idx) != (i, j):
					return False

		return checker_helper(i, j + 1)

	return checker_helper(0, 0)


def is_valid_sudoku_epi(A):
	def has_duplicate(block):
		block = filter(lambda x: x != 0, block)
		return len(block) != len(set(block))

	n = len(A)
	if any(
		has_duplicate([A[i][j] for j in range(n)])
		or has_duplicate([A[j][i] for j in range(n)])
		for i in range(n)):
		return False

	region_size = int(math.sqrt(n))
	return all(not has_duplicate([
		A[i][j]
		for i in range(region_size * I, region_size * (I + 1))
		for j in range(region_size * J, region_size * (J + 1))
		]) for I in range(region_size) for J in range(region_size))


def is_valid_sudoku_pythonic(A):
	"""
	For each non-zero value in A, we need to check if there's a duplicate
	of this value in its row, column, and subgrid. For that, we define
	three tuples for each non-zero assignment
	
	Say that we have 5 at i, j, we define the following three
	tuples:
		row: (i, '5')
		col: ('5', j)
		subgrid: (i // 3, j // 3, '5')

	And count the occurrences of each of these tuples, if the count for
	any of the tuples at any position or number is > 1, then there must
	certainly be duplicates
	"""
	region_size = int(math.sqrt(len(A)))
	return max(collections.Counter(
		k for i, row in enumerate(A)
		for j, c in enumerate(row) if c != 0
		for k in ((i, str(c)), (str(c), j),
			(i // region_size, j // region_size, str(c)))
		).values(), defualt=0) <= 1


sudoku = [[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,9]]

print(is_valid_sudoku(sudoku))

