import random


def random_subset_brute_force(n, k):
	"""
	The optimal solution can be as optimal as O(k) time and space complexity

	This brute force solution takes O(n) to create the array and O(n) to shuffle,
	and O(n) space storing the size-n array
	"""
	A = list(range(n))
	random.shuffle(A)

	return A[:k]


def random_sampling(n, k):
	"""
	Time complexity:
		O(n) for array generation, and takes k swaps --> O(n)
	Space complexity:
		O(n)
	"""
	A = list(range(n))
	for i in range(k):
		r = random.randint(i, n - 1)
		A[i], A[r] = A[r], A[i]
	return A[:k]


def random_subset(n, k):
	"""
	Find a way to avoid creating an array of size n, this will
	then reduce both time and space complexity to O(k)

	Generate random indices and move the values from that indice
	in A to the begining of the array to return

	In order to do this without actually having A is to use hasing
	and record those indices where swaps have been performed
	"""
	changed_elements = {}
	for i in range(k):
		rand_idx = random.randint(i, n - 1)
		rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
		i_mapped = changed_elements.get(i, i)

		changed_elements[rand_idx] = i_mapped
		changed_elements[i] = rand_idx_mapped

	return [changed_elements[i] for i in range(k)]


print(random_subset(100, 4))


