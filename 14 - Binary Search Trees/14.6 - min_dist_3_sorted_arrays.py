import heapq


def find_closest_elements_in_sorted_arrays(sorted_arrays):
	class Element:
		def __init__(self, num, it):
			self.num = num
			self.it = it

		def __lt__(self, other):
			return self.num < other.num

	triples = []
	for arr in sorted_arrays:
		it = iter(arr)
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(triples, Element(first_element, it))

	min_dist_so_far = float('inf')
	while True:
		min_element = heapq.heappop(triples)
		max_element = max(triples)
		min_dist_so_far = min(min_dist_so_far, max_element.num - min_element.num)
		next_min_val = next(min_element.it, None)
		if next_min_val is None:
			return min_dist_so_far
		heapq.heappush(triples, Element(next_min_val, min_element.it))

