"""
Given a list of arrays where the nth array contains n elements.
Such list forms a triangle and the aim of this problem is to find
the minimum weighted path from the top of the triangle to the
bottom. When moving up or down, only adjacent positions of the
from the adjacent rows can be reached.

					 2
					4 4
				   8 5 6
				  4 3 6 2
				 1 5 2 3 4

The minimum weighted path for this triangle is:
			2 + 4 + 5 + 2 + 2 = 15

The brute-force implementation is the find all possible paths while
computing the sum of their weights. Compare the sum of weights to
a global minimum when the bottom is reached.

This solution has an exponential time complexity since for each
position in a triangle, except both left and right extremes, there
are always two possible ways to descend.

Recursion with memorization is used to cache intermediate results
to avoid repeated computions.
"""
import functools


def minimum_weight_path_in_triangle_brute_force(triangle):
	def descend_in_triangle(row, col, curr_min_weight):
		"""
		Time complexity:
			O(2 ** n), with n being the height of
			the triangle
		"""
		if row == len(triangle):
			return curr_min_weight
		curr_min_weight += triangle[row][col]
		return min(descend_in_triangle(row + 1, col, curr_min_weight),
		descend_in_triangle(row + 1, col + 1, curr_min_weight))
	return descend_in_triangle(0, 0, 0)


def minimum_weight_path_in_triangle_n2_space(triangle):
	"""
	O(n^2) time and space complexity
	There are n * (n - 1) / 2 elements and time
	spent on each is O(1)
	"""
	@functools.lru_cache(None)
	def minimum_weight_path_from_pos(row, col):
		if row == len(triangle) - 1:
			return triangle[row][col]
		return (triangle[row][col] +
					min(minimum_weight_path_from_pos(row + 1, col),
						minimum_weight_path_from_pos(row + 1, col + 1)))
	return minimum_weight_path_from_pos(0, 0) if triangle else 0


def minimum_weight_path_in_triangle_n_space(triangle):
	min_weight_to_curr_row = [0]
	for row in triangle:
		min_weight_to_curr_row = [
			row[j] + min(
				min_weight_to_curr_row[max(j - 1, 0)],
				min_weight_to_curr_row[min(j, len(row) - 2)])
			for j in range(len(row))
		]
	return min(min_weight_to_curr_row)


triangle = [[2],[4,4],[8,5,6],[4,2,6,2],[1,5,2,3,4]]
print(minimum_weight_path_in_triangle(triangle))

