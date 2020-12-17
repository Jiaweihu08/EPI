import random

def random_sampling(k, A):
	for i in range(k):
		r = random.randint(i, len(A) - 1)
		A[i], A[r] = A[r], A[i]


def compute_random_permutation(n):
	permutation = list(range(n))
	random_sampling(n, permutation)
	return permutation


print(compute_random_permutation(5))