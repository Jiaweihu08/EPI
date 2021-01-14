import functools


def fibonacci_naive(n):
	"""
	O(2**n) time complexity
	O(1) space complexity
	"""
	if n <= 1:
		return n
	return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# @functools.cache # new in version 3.9
@functools.lru_cache(None)
def fibonacci_cached(n):
	"""
	O(n) time complexity
	O(n) space complexity
	"""
	if n <= 1:
		return n
	return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def fibonacci_efficient(n):
	"""
	O(n) time complexity
	O(1) space complexity
	"""
	if n <= 1:
		return n

	f_minus_2, f_minus_1 = 0, 1
	for _ in range(n):
		f = f_minus_2, f_minus_1
		f_minus_2, f_minus_1 = f_minus_1, f
	return f_minus_1


# Given an array of integers, find the maximum sum over all subarrays


def find_max_sum_n3(A):
	"""
	Compute the sum of all possible subarrays: n(n-1)/2
	O(n**3) time complexity
	"""
	result = float('-inf')
	for size in range(1, len(A)):
		for start_idx in range(len(A) - size):
			result = max(result, sum(A[start_idx:start_idx + size]))
	return result


def find_max_sum_n2(A):
	"""
	The same methodology as before but range sum is computed
	via S which is an accumulated sum of A.
	"""
	S = [0] * (len(A) + 1)
	for i, a in enumerate(A):
		S[i] = S[i - 1] + a

	result = float('-inf')
	for size in range(1, len(A)):
		for j in range(size, len(A)):
			result = max(result, S[j] - S[j - size - 1])
	return result


def find_max_sum_dp(A):
	# A.append(0)
	# max_val = float('-inf')
	# for i in range(len(A) - 1):
	# 	A[i] = max(A[i - 1] + A[i], A[i])
	# 	max_val = max(max_val, A[i])
	# return max_val

	max_seen = max_end = 0
	for a in A:
		max_end = max(max_end + a, a)
		max_seen = max(max_seen, max_end)
	return max_seen


A = [904, 40, 523, 12, -385, -124, 481, -31]
print(find_max_sum_dp(A))