"""
Given a max-heap, represented as an array, return the k largest elements from the
heap without modifying the array

The amount of ordering information stored in heaps are limited, but we know that
the next largest element has to be either the left or right child of the current
max element, and the largest element in the entire array is at its index 0

Store the left and right chil in a max heap together with their indices and each
time extract the max element from it

O(nlog(k)) Time complexity
O(log(k)) Space complexity
"""
import heapq


def k_largest(A, k):
	if k <= 0:
		return []

	candidate_max_heap = [(-A[0], 0)]
	result = []
	for _ in range(k):
		candidate_idx = candidate_max_heap[0][1]
		result.append(-heapq.heappop(candidate_max_heap)[0])

		left_child_idx = 2 * candidate_idx + 1
		if left_child_idx < len(A):
			heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))

		right_child_idx = 2 * candidate_idx + 2
		if right_child_idx < len(A):
			heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

	return result


A = [561, 314, 401, 28, 156, 359, 271, 11, 3]
k = 4
print(k_largest(A, k))