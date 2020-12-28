"""
Sort k-sorted arrays
Each element in the array can not be more than k positions
away from their sorted position
"""
import itertools
import heapq


def sort_almost_sorted_array(sequence, k):
	min_heap = []

	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap, x)

	results = []
	for x in sequence:
		results.append(heapq.heappushpop(min_heap, x))

	while min_heap:
		results.append(heapq.heappop(min_heap))
	return results
