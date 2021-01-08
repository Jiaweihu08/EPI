"""
Given an array of integers, find the length of the longest nondecreasing
subsequence in the array
"""
import bisect


def longest_nondecreasing_subsequence_n2(A):
	max_length = [1] * len(A)
	for i in range(len(A)):
		max_length[i] = 1 + max(
			(max_length[j] for j in range(i) if A[i] >= A[j]), default=0)
	return max(max_length)


def longest_nondecreasing_subsequence_nlogn(A):
	nondecreaseing_subsequence = []
	for num in A:
		position = bisect.bisect_right(nondecreaseing_subsequence, num)
		if position == len(nondecreaseing_subsequence):
			nondecreaseing_subsequence.append(num)
		else:
			nondecreaseing_subsequence[position] = num
	return len(nondecreaseing_subsequence)


A = [0,8,4,12,2,10,6,14,1,7,7,9]
print(longest_nondecreasing_subsequence_nlogn(A))

