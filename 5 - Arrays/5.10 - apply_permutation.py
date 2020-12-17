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
	need to now keep swapping until an 0 is found at i

	If the value at index 2 is 0, then the next swap will result in the
	following perm = [0,_,2,3, ...], and we now move on to the next index
	i = 1

	At each swap we also do the same swapping for A
	"""
	for i in range(len(A)):
		while perm[i] != i:
			A[i], A[perm[i]] = A[perm[i]], A[i]
			perm[i], perm[perm[i]] = perm[perm[i]], perm[i]


A = ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'h']
perm = [3,7,5,2,0,4,1,6]
permute_array(A, perm)
print(A)

