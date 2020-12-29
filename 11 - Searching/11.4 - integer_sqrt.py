"""
Given an integer k, return the largest integer whose aquare is smaller than x
"""
import math


def square_root_naive(k):
	return math.floor(math.sqrt(k))


def square_root(k):
	# if k in (0, 1):
	# 	return k

	# left, right = 0, k
	# while left <= right:
	# 	mid = (left + right) // 2
	# 	mid_squared = mid * mid
	# 	if mid_squared == k or mid == l:
	# 		return mid
	# 	if mid_squared < k:
	# 		l = mid
	# 	else:
	# 		r = mid - 1

	left, right = 0, k
	while left <= right:
		mid = (left + right) // 2
		mid_squared = mid * mid
		if mid_squared <= k:
			# values from [0, m] are less or equal than sqrt of k
			left = mid + 1
		else:
			# values from [0, m] are greater that sqrt of k
			right = mid - 1
	return left - 1


print(square_root(300))


