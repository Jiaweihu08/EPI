"""
Given a stream of integers, return the median at each read

Given an array of integers in non-decreasing order, the median
is the mean of the two values in the middle

Values are stored in two heaps, a min_heap and a max_heap
The smaller half is stored in the max_heap and the larger half
in the min_heap. To compute the median, calculate the mean of
 max_heap[0] and min_heap[0]

O(nlog(k)) Time complexity
O(log(k)) Space complexity
"""
import heapq


def online_median(sequence):
	min_heap = []
	max_heap = []
	result = []
	
	for x in sequence:
		heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
		
		if len(max_heap) > len(min_heap):
			heapq.heappush(min_heap, -heapq.heappop(max_heap))

		result.append(0.5 * (min_heap[0] + (-max_heap[0]))
			if len(min_heap) == len(max_heap) else min_heap[0])
	return result


seq = iter([1,0,3,5,2,0,1])
print(online_median(seq))
