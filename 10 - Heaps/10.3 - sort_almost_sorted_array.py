"""
Write a programm to sort k-sorted arrays, where each element
in the array cannot be more than k positions away from their
sorted position

For each position i in A, only elements from range
[i-k/2, i+k/2] are to be considered. Instead of comparing each
entry with all other entries in the array, there are only k
comparisons needed at max. We use a min heap to store k elements
and at each iteration we pop the smallest one and store it in
the results.

Given an array with n elements, the time complexity is O(nlog(k)),
and the space complexity if O(log(k))
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


# Tested with EPIJudge
