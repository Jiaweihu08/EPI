"""
Given a stream of integers, return the median at each read. You cannont go
back and read previous values
"""
import heapq


def online_median(sequence):
	min_heap = []
	max_heap = []
	results = []
	
	for x in sequence:
		heapq.heappush(max_heap, -heappushpop(min_heap, x))

		if len(max_heap) > len(min_heap):
			heapq.heappush(min_heap, -heappop(max_heap))

		results.append(0.5 * (min_heap[0] + max_heap[0] if len(min_heap) == 
			len(max_heap) else min_heap[0]))
	return results