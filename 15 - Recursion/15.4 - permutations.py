"""
Compute all permutations of a list of integers

The most straightforward approach is to iterate through the
list, move the current item to the front and append all the permutations
of the rest of the elements to it

By using recursion we can keep reducing the number of items in the list
until the input size is one
"""

# def compute_permutations(nums):
# 	def permutation_helper(remaining_nums):
# 		if len(remaining_nums) == 1:
# 			return [remaining_nums]
# 		permutations = []
# 		for j in range(len(remaining_nums)):
# 			for subperm in permutation_helper(remaining_nums[:j] + remaining_nums[j+1:]):
# 				permutations.append([remaining_nums[j]] + subperm)
# 		return permutations
# 	return permutation_helper(nums)


# print(compute_permutations([1,2,3,4]))


def permutations(A):
	def directed_permutations(i):
		if i == len(A) - 1:
			results.append(A.copy())
			return

		for j in range(i, len(A)):
			# with A = [1,2,3,4] here we are computing the permutations
			# of the last three elements of the following lists:
			# [1,2,3,4], [2,1,3,4], [3,1,2,4], [4,1,2,3]
			# This is achieved by swapping elements at i and j positions
			A[i], A[j] = A[j], A[i]
			directed_permutations(i+1)
			A[i], A[j] = A[j], A[i]

	results = []
	directed_permutations(0)
	return results

print(compute_permutations([1,2,3,4]))


