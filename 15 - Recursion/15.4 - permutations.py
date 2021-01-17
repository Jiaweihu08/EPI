"""
Compute all permutations of a given list of integers.

If the given list is [1,2,3] then all permutations of this list are:
[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1].

The most straightforward approach is to iterate through the
list, move the current item to the front and append all the permutations
of the rest of the elements to it.

By using recursion we can keep reducing the number of items in the
list until the input size is one.

The time complexity for both implementations shown below is O(n x n!).
At each recursion call we have n - i iterations, and for each we spent
another n - i - 1 calls in its loop. With n, the length of the input
array A, being 4, in the first recursion call on i = 0 we do 3 recursion
calls on i = 1. This in turn does 2 recursion calls on i = 2, etc.
"""
def compute_permutations(A):
	def permutations_for_subarray(remaining_nums):
		if len(remaining_nums) == 1:
			return [remaining_nums]
		
		permutations = []
		for j in range(len(remaining_nums)):
			for subperm in permutations_for_subarray(
				remaining_nums[:j] + remaining_nums[j + 1:]):
				permutations.append([remaining_nums[j]] + subperm)
		return permutations
	return permutations_for_subarray(A)


def permutations(A):
	def directed_permutations(i):
		if i == len(A) - 1:
			results.append(A.copy())
			return

		for j in range(i, len(A)):
			A[i], A[j] = A[j], A[i]
			directed_permutations(i + 1)
			A[i], A[j] = A[j], A[i]

	results = []
	directed_permutations(0)
	return results


def find_permutations_via_next_permutaion(A):
	"""
	First sort the input array in nondecreasing order then keep adding
	its next permutations that's larger than itself lexicographically
	to the result.
	"""
	def next_permutation(perm):
		"""
		The next permutaion of a given permutation is the smallest
		permutation that's larger than the given permutation in a
		lexicographical order.

		In order to find the next permutation, the lexicographical order
		of the permutation has to be increased as little as possible by
		swapping with entries from itself.
		
		e.g. The next permutations of [0,1,2] is [0,2,1], and not [2,0,1].
		The increase lead by swapping 1 and 2 is the smallest possible.

		In order to do that, we find the element starting from the right
		that's smaller that the one located on its right side(start
		looking from len(A) - 2) and call the index of this element the
		inversion point.


		- input perm: [6,4,5,0,3,2,1]
							 ^
		- inversion element: 0 => inversion point: 3 


		If such element doesn't exist(reaching index -1), then return an
		empty list meaning the next permutation doesn't exist. The given
		permutaions is in decreasing order from left to right, so no
		permutation can be lexicographically larger.

		Otherwise, find the smallest entry larger than the inversion
		element located on it's right side, and swap the two. Since the
		original inversion element is the smallest from its position and
		beyond, after the swap the entries on its right are still in
		nonincreasing order.

		- swap 0 with the smallest larger element on its right, which is
		1:  ==> [6,4,5,1,3,2,0].

		To finish the process, reverse the remaining entries from the
		inversion point:
				[6,4,5,1,0,2,3]
		"""
		inversion_point = len(perm) - 2
		while (inversion_point >= 0
			and perm[inversion_point] >= perm[inversion_point + 1]):
			inversion_point -= 1
		if inversion_point == -1:
			return []

		for i in reversed(range(inversion_point + 1, len(perm))):
			if perm[i] > perm[inversion_point]:
				(perm[i], perm[inversion_point] = perm[inversion_point], perm[i])
				break
		perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
		return perm
	
	A.sort()
	result = []
	while True:
		result.append(A.copy())
		A = next_permutation(A)

		if not A:
			break
	return result


print(permutations([1,2,3,4]))
