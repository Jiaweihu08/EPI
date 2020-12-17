def n_queens(n):
	def solve_n_queens(row):
		if row == n:
			results.append(col_placements.copy())
			return
		for col in range(n):
			valid = True
			for i, c in enumerate(col_placements[:row]):
				if abs(col - c) in (0, row - i):
					valid = False
					break
			if valid:
				col_placements[row] = col
				solve_n_queens(row+1)

	results = []
	col_placements = [0] * n
	solve_n_queens(0)
	return results


if __name__ == '__main__':
	print(n_queens(5))