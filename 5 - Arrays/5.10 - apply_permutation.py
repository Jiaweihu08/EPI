"""
Given an array of integers A and a permutation array perm
of the same size where each entry defines the index position
that the same entry in A should be

e.g. A = [1,2,3] perm = [2,0,1] --> [2,3,1]

Define a function to apply the permutation array perm to A
"""


def permute_array_naive(A, perm):
	permuted_array = [0] * len(A)
	for i in range(len(A)):
		permuted_array[perm[i]] = A[i]
	return permuted_array


def permute_array(A, perm):
	"""
	For each index value from perm, iteratively move the current
	value to the index defined by its value

	Say that we have the following perm = [3,_,_,2, ...] and i = 0

	The value of perm at i is perm[i] = perm[0] = 3, we swap the value
	of perm at i with the value of perm at perm[i] = 3

	The resulting perm is now perm = [2,_,_,3, ...], what is achieved
	by the swap here is that 3 is now at its correct position, and we
	need to now keep swapping until an 0 is found at i(=0)

	If the value at index 2 is 0, then the next swap will result in the
	following perm = [0,_,2,3, ...], and we now move on to the next index
	i = 1

	At each swap we also do the same swapping for A

	------------

	Pay attention to how the swapping elements from a list works internally
	in python in order to avoid mistakes

	A = [4,1,0,3,2]
	1) A[A[0]], A[0] = A[0], A[A[0]]
	2) A[0], A[A[0]] = A[A[0]], A[0]

	The first one will work just fine yielding A = [2,1,0,3,4], but the second
	one will not give the expected result: A = [2,1,4,3,2]

	A high-level intuition is that the right side of the equal sign
	when swapping elements like this is stored in a stack with the elements
	pushed from right to left, then the values are popped to be assigned

	A[0] is first updated to be the value of A[A[0]] = A[4] = 2, but A[A[0]]
	will not give us A[4] but A[2], since now A[0] = 2

	The right hand side is stored in the stack and the swapping happened on the
	left won't change their values
	"""
	for i in range(len(A)):
		while perm[i] != i:
			A[perm[i]], A[i] = A[i], A[perm[i]]
			perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
			
			


A = ['a', 'b', 'c', 'd']
perm = [2,0,1,3]
permute_array(A, perm)
print(A)
