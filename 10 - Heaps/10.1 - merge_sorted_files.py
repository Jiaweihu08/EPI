"""
Given k sorted arrays, merge them into a single sorted array

Since all arrays are sorted, we can use merge sort implemented
with a min heap.

We store the first element of all arrays in a min heap and keep
extracting the smallest one and append it to the result. The next
element from the popped element pertains to is added back to the
heap.

There are n elements in total and each heap modifications is log(k)
with k being the height of the heap.

O(nlog(k)) Time complexity
O(log(k)) Space complexity
"""
import heapq


def merge_sorted_arrays(sorted_arrays):
	min_heap = []
	sorted_arrays_iters = [iter(arr) for arr in sorted_arrays]

	for i, it in enumerate(sorted_arrays_iters):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))

	results = []
	while min_heap:
		smallest_entry, smallest_array_index = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iters[smallest_array_index]
		results.append(smallest_entry)
		next_entry = next(smallest_array_iter, None)
		if next_entry is not None:
			heapq.heappush(min_heap, (next_entry, smallest_array_index))

	return results


# Test the code with EPIJudge
