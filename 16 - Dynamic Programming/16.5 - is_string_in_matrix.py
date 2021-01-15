import functools


# import collections
# Position = collections.namedtuple('Position', ('row', 'col'))
# def is_string_in_matrix(grid, pattern):
# 	@functools.lru_cache(None)
# 	def is_string_in_position(pos, i):
# 		if grid[pos.row][pos.col] == pattern[i]:
# 			print(pos)
# 			if i == len(pattern) - 1:
# 				return True
			
# 			positions = []
# 			if pos.row > 0:
# 				positions.append(Position(pos.row - 1, pos.col))
# 			if pos.row < len(grid) - 1:
# 				positions.append(Position(pos.row + 1, pos.col))
# 			if pos.col > 0:
# 				positions.append(Position(pos.row, pos.col - 1))
# 			if pos.col < len(grid[0]) - 1:
# 				positions.append(Position(pos.row, pos.col + 1))

# 			for position in positions:
# 				if is_string_in_position(position, i + 1):
# 					return True
# 		return False

# 	for row in range(len(grid)):
# 		for col in range(len(grid[0])):
# 			if is_string_in_position(Position(row, col), 0):
# 				return True
# 	return False


def is_string_in_matrix(grid, pattern):
	@functools.lru_cache(None)
	def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
		if offset == len(pattern):
			return True

		if (not (0 <= x < len(grid) and 0 <= y < len(grid[x]))
				or grid[x][y] != pattern[offset]):
			return False

		return any(
			is_pattern_suffix_contained_starting_at_xy(*next_xy, offset + 1)
			for next_xy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

	return any(
		is_pattern_suffix_contained_starting_at_xy(i, j, 0)
		for i in range(len(grid)) for j in range(len(grid[i])))



grid = [[1,2,3],[3,4,5],[5,6,7]]
pattern = [1,3,4,6]
print(is_string_in_matrix(grid, pattern))