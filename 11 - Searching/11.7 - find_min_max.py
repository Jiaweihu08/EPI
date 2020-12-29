"""
Given an array of integers, return the min and max with less
than 2(n - 1) comparisons
"""

import collections


MinMax = collections.namedtuple('MinMax', ('min', 'max'))


def find_min_max(A):
	"""
	Split the array into pairs of two and find the max and min
	for each pair. The global max will be the max of all maxs
	from pairs, similarly for the global min.
	(3n/2 - 2) < 2(n - 1) comparisons
	"""
	def min_max(a, b):
		return MinMax(a, b) if a < b else MinMax(b, a)

	if len(A) <= 1:
		return min_max(A[0], A[0])

	global_min_max = min_max(A[0], A[1])

	for i in range(2, len(A) - 1, 2):
		local_min_max = min_max(A[i], A[i + 1])
		global_min_max = MinMax(
			min(global_min_max.min, local_min_max.min),
			max(global_min_max.max, local_min_max.max))

	if len(A) % 2:
		global_min_max = MinMax(
			min(global_min_max.min, A[-1]),
			max(global_min_max.max, A[-1]))

	return global_min_max