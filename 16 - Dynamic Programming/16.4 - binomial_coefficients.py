"""
Design an efficient algorithm for computing binomial coefficients
which has the property that it never overflows if the final result
fits in the integer word size.

The binomial coefficient is the number of ways to choose a k-element
subset from an n-element set.

Consider the nth element from the n-element set. A subset of size
k will either contain this element, or not contain it. We first
compute subset of size k - 1 amongst the first n - 1 elements and
add the nth element into these sets, and then find all subsets of
size k amongst the first n - 1 elements.

with n = 5, k = 3, first we find all subsets of size 2 from [1,2,3,4]
and add 5 to each of these subsets, and then we compute subsets of
size 3 from [1,2,3,4]. The result is the union of these two sets of
subsets.

Recursion is used to implement the algorithm. 
"""
import functools


@functools.lru_cache(None)
def compute_binomial_coefficient(n, k):
	"""
	Space and time complexity: O(nk)
	"""
	if k in (0, n):
		return 1

	without_k = compute_binomial_coefficient(n - 1, k)
	with_k = compute_binomial_coefficient(n - 1, k - 1)
	return without_k + with_k


# def compute_binomial_coefficient_k_space(n, k):
# 	dp = [0] * (k + 1)
# 	dp[0] = 1
# 	for i in range(1, n + 1):
# 		last_without_k = dp[0]
# 		for j in range(1, k + 1):
# 			if j > i:
# 				break
# 			dp[j], last_without_k = dp[j] + last_without_k, dp[j]
# 	return dp[-1]


print(compute_binomial_coefficient(5, 4))