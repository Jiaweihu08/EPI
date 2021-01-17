"""
steps:
- Find the next empty position
- Try out possible values until the assignment is completed
"""
def sudoku_solver(sudoku):
	def solve_partial_sudoku(i, j):
		if j == 9:
			j = 0
			i += 1
			if i == 9:
				return True

		if sudoku[i][j] != 0:
			return solve_partial_sudoku(i, j+1)

		def is_valid(i, j, val):
			#check if val is valid for row
			if val in sudoku[i]:
				return False
			#check if val is valid for col
			for row in sudoku:
				if row[j] == val:
					return False
			#ckeck if val is valid for subgrid
			min_row, max_row = 3 * (i // 3), 3 * (i // 3 + 1)
			min_col, max_col = 3 * (j // 3), 3 * (j // 3 + 1)
			for row in sudoku[min_row:max_row]:
				if val in row[min_col:max_col]:
					return False

			return True

		for val in range(1, 10):
			if is_valid(i, j, val):
				sudoku[i][j] = val
				if solve_partial_sudoku(i, j+1):
					return True

		sudoku[i][j] = 0
		return False
	
	solve_partial_sudoku(0, 0)
	return sudoku


sudoku = [[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,9]]

print(sudoku_solver(sudoku))
