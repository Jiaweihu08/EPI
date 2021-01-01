"""
Given a set of integers, find the length of the largest subarray satisfying
the condition that is two elements are in the array so are all integers
between them
"""
def longest_contained_range_n3(A):
	"""
	Take all pairs of integers from A and test if all values from the defined
	range are in A

	O(n^3) time complexity
	"""
	all_integers = set(A)
	A.sort()
	result = 1
	for i, smaller in enumerate(A[:-1]):
		try_larger = True
		for larger in A[i + 1:]:
			if smaller == larger:
				continue

			for num in range(smaller + 1, larger):
				if num not in all_integers:
					try_larger = False
					break
			else:
				result = max(result, larger - smaller + 1)
			if not try_larger:
				break
	return result


def longest_contained_range_n2(A):
	"""
	For each element in the array, compute its largest value that satisfies
	the conditions, making sure that it's contained in the array
	
	Compute their differences and update result if needed
	"""
	all_integers = set(A)
	result = 1
	for left in A:
		right = left + 1
		if right in A:
			while right + 1 in A:
				right += 1
			result = max(result, right - left + 1)
	return result


def longest_contained_range(A):
	"""
	Iterate through the array and for each value find the largest satisfying
	interval extending from both sides
	"""
	unprocessed_entries = set(A)
	max_interval_size = 0
	while unprocessed_entries:
		a = unprocessed_entries.pop()

		lower_bound = a - 1
		while lower_bound in unprocessed_entries:
			unprocessed_entries.remove(lower_bound)
			lower_bound -= 1

		upper_bound = a + 1
		while upper_bound in unprocessed_entries:
			unprocessed_entries.remove(upper_bound)
			upper_bound += 1

		max_interval_size = max(max_interval_size,
						upper_bound - lower_bound - 1)
	return max_interval_size



# A = [2, 1]
# A = [3, 0, 1, 2, 5, 6]
A = [17, 26, 19, 32, 28, 6, 19, 15, 30, 6, 11, 33, 32, 34, 9, 1, 9, 11,
		2, 30, 33, 6, 18, 19, 20, 27, 11, 7, 35, 0, 31, 12, 33, 30, 24]
print(longest_contained_range(A))

