"""
Given an array of integers, return the kth largest element

The naive solution would be sort the array in descending order
and return the element at k-1 index, the time complexity is
O(nlog(n))

Another way to solve this is to store candidate elements in a
k-size min-heap. The time complexity is O(nlog(k)) and O(k)
space complexity. But again, it stores k largest elements.
"""
import random


def find_kth_largest(A, k):
	"""
	Randomly select an element and partition the array into elements
	greater than k and smaller than k. If the number of elements greater
	than k is k - 1, then the current element is the one we look for. If
	the number is smaller, this means that we should look on the right side
	of the partitioned array, and the left side if the number is larger.
	"""
	def partition_around_pivot(left, right, pivot_idx):
		pivot = A[pivot_idx]
		new_pivot_idx = left
		A[right], A[pivot_idx] = A[pivot_idx], A[right]
		for i in range(left, right):
			if A[i] > pivot:
				A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
				new_pivot_idx += 1
		A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
		return new_pivot_idx

	left, right = 0, len(A) - 1
	while left <= right:
		pivot_idx = random.randint(left, right)
		new_pivot_idx = partition_around_pivot(left, right, pivot_idx)

		if new_pivot_idx == k - 1:
			return A[new_pivot_idx]
		elif new_pivot_idx > k - 1:
			right = new_pivot_idx - 1
		else:
			left = new_pivot_idx + 1


print(find_kth_largest([3,1,-1,2], 1))

