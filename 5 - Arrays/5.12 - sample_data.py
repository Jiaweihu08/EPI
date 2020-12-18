"""
Given an array of distinct elements and a size k, return a
subset of size k, making sure that all possible subsets of
size k are equally likely to be chosen
"""
import random


def random_samping(A, k):
	"""
	At each iteration, choose a number randomly and add
	it to the partial subset. At the next iteration, the
	number to add is chosen from the remaining numbers.
	"""
	for i in range(k):
		r = random.randint(i, len(A) - 1)
		A[i], A[r] = A[r], A[i]


A = [0,1,2,3,4,5,6,7,8]
random_samping(A, 4)
print(A)