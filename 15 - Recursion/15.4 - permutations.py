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
			A[i], A[j] = A[j], A[i]
			directed_permutations(i+1)
			A[i], A[j] = A[j], A[i]

	results = []
	directed_permutations(0)
	return results

print(permutations([1,2,3,4]))