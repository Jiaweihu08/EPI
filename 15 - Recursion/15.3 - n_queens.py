"""
Place n queens on a n x n board in nonattacking positions

Nonattacking positions means that no two queens are placed
in the same row, column, or diagonal

For n = 4, here is a posible solution of the problem:
_ x _ _
_ _ _ x
x _ _ _
_ _ x _

Since there can only be one queen for each row, we can define
our outputs as a n-length list with each value being the column
where the queen is placed

For each row, we iterate through the columns and check if the
current placement is acceptable
"""


def n_queens(n):
	def solve_n_queens(row):
		if row == n:
			results.append(col_placement.copy())
			return
		for col in range(n):
			# A more pythonic version to check the validity of the
			# current col
			
			# if all(
			# 	abs(c - col) not in (0, row - i) 
			# 	for i, c in enumerate(col_placement[:row])):
				
			# 	col_placement[row] = col
			# 	solve_n_queens(row+1)
			
			for i, c in enumerate(col_placement[:row]):
				if abs(col - c) in (0, row - i):
					break
			else:
				col_placement[row] = col
				solve_n_queens(row+1)


	results = []
	col_placement = [0] * n
	solve_n_queens(0)
	return results


print(n_queens(4))