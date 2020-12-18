"""
Given an integer n, return a random permutation of
[1,2,..., n - 1]. All possible permutations should
have the same probability to be chosen
"""
import random


def compute_random_permutation(n):
	def random_sampling(k, A):
		for i in range(k):
			r = random.randint(i, len(A) - 1)
			A[i], A[r] = A[r], A[i]
			
	permutation = list(range(n))
	random_sampling(n, permutation)
	return permutation


print(compute_random_permutation(5))