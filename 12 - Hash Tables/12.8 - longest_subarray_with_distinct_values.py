"""
Given an array and find the longest subarray that all of its values
are distincs

e.g.
A = ['f','s','f','e','t','w','e','n','w','e'] ==> ['s','f','e','t','w']
"""
# def find_longest_subarray_with_distinct_values_n3(A):
# 	max_len = 0
# 	for subarray_size in range(len(A)):
# 		for start_idx in range(len(A)):
# 			subarray = A[start_idx:start_idx + subarray_size]
# 			num_distinct_vals = len(set(subarray))
# 			if (num_distinct_vals == subarray_size and
# 					max_len < num_distinct_vals):
# 				max_len = num_distinct_vals
# 	return max_len


def find_longest_subarray_with_distinct_values_n2(A):
	max_len = 0
	for start_idx in range(len(A)):
		distinct_values = set()
		for i, a in enumerate(A[start_idx:]):
			if a in distinct_values:
				max_len = max(i, max_len)
				break
			distinct_values.add(a)
		else:
			max_len = max(len(distinct_values), max_len)

	return max_len


def find_longest_subarray_with_distinct_values(A):
	"""
	Iterate through the array and keep adding entries to a hash
	table until a repeated value if found. Compute the length of
	the subarray and update the value if neede

	The next subarray to be considered is the current one reduced
	from the left side until the index where the repeated entry was
	last found is passed. Once done, we keep growing the subarray
	on the right until a new repeat is found
	"""
	most_recent_occurrence = dict()
	dup_free_subarray_start_idx = result = 0
	for i, a in enumerate(A):
		if a in most_recent_occurrence:# found a repeating entry
			result = max(i - dup_free_subarray_start_idx, result)
			dup_idx = most_recent_occurrence[a]
			# removing entries that appeared before the current
			# elements' most recent occurrence
			for key, idx in most_recent_occurrence.copy().items():
				if idx < dup_idx:
					del most_recent_occurrence[key]
			dup_free_subarray_start_idx = dup_idx + 1
		most_recent_occurrence[a] = i		
	return max(result, len(most_recent_occurrence))


def find_longest_subarray_with_distinct_values_epi(A):
	"""
	In the previous implementation, a hash table is used to check
	for duplicates in the subarray, when a duplicate is found, we
	update the left limit of the subarray to the next position of
	the last occurrence of this entry. Since a new subarray is
	considered, the elements before its left limit shoud not be in
	the hash table, thus iterating through the table and removing
	them are required.

	If we think carefully, this is actually necessary. Even if an
	element is in the hash table, if its most recent occurrence is
	before the left limit, it should be considered as a repeat and
	we don't need to update the left limit.
	"""
	most_recent_occurrence = dict()
	dup_free_subarray_start_idx = result = 0
	for i, a in enumerate(A):
		if a in most_recent_occurrence:
			dup_idx = most_recent_occurrence[a]
			if dup_idx >= dup_free_subarray_start_idx:
				result = max(result, i - dup_free_subarray_start_idx)
				dup_free_subarray_start_idx = dup_idx + 1
		most_recent_occurrence[a] = i
	return result



A = ['f','s','f','e','t','w','e','n','w','e']
print(find_longest_subarray_with_distinct_values_epi(A))

