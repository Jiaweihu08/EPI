"""
Given k sorted arrays, merge them into a single sorted array
"""
import heapq


def merge_sorted_arrays(sorted_arrays):
	min_heap = []
	sorted_arrays_iters = [iter(arr) for arr in sorted_arrays]

	for i, it in enumerate(sorted_arrays_iters):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (i, first_element))

	results = []
	while min_heap:
		smallest_entry, smallest_array_index = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iters[smallest_array_index]
		results.append(smallest_entry)
		next_entry = next(smallest_array_iter, None)
		if next_entry is not None:
			heapq.heappush(min_heap, (next_entry, smallest_array_index))

	return results

