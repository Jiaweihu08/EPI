"""
Given an array of strings and a array containing keywords, return the
indices of start and end of the smallest subarray that contains all
keywords in the same order as they appear in the keyrwords array


"""
import collections


Subarray = collections.namedtuple('Subarray', ('start', 'end'))


# def find_smallest_sequentially_covering_subset_n3(paragraph, keywords):
# 	"""
# 	Iterate over all possible subarrays and check if they cover the keywords
# 	sequentially

# 	O(n^3) time complexity
# 	"""
# 	result = Subarray(-1, -1)
# 	for size in range(len(paragraph) + 1):
# 		for start_idx in range(len(paragraph)):
# 			keyword_index = 0
# 			for i, word in enumerate(paragraph[start_idx:start_idx + size]):
# 				if keyword_index == len(keywords):
# 					break
# 				if word == keywords[keyword_index]:
# 					if keyword_index == 0:
# 						start = i + start_idx
# 					elif (keyword_index == len(keywords) - 1 and
# 							(result == Subarray(-1, -1) or
# 								i + start_idx - start < result.end - result.start)):
# 						result = Subarray(start, i + start_idx)
# 					keyword_index += 1
# 	return result


def find_smallest_sequentially_covering_subset_n2(paragraph, keywords):
	"""
	Grow subarrays starting from all possible positions incrementally until
	either the end is reached of the keywords are found sequentially

	O(n^2) time complexity
	"""
	last_start_idx = len(paragraph) - len(keywords) + 1
	result = Subarray(-1, -1)
	for start_idx in range(last_start_idx):
		keyword_index = 0
		for i, word in enumerate(paragraph[start_idx:]):
			if keyword_index == len(keywords):
				break
			if word == keywords[keyword_index]:
				if keyword_index == 0:
					start = i + start_idx
				elif (keyword_index == len(keywords) - 1 and 
						(result == Subarray(-1, -1) or
							i + start_idx - start < result.end - result.start)):
					result = Subarray(start, i + start_idx)
				keyword_index += 1
	return result


def find_smallest_sequentially_covering_subset(paragraph, keywords):
	keyword_to_idx = {k: i for i, k in enumerate(keywords)}
	latest_occurrence = [-1] * len(keywords)
	shortest_subarray_length = [float('inf')] * len(keywords)
	shortest_distance = float('inf')
	result = Subarray(start=-1, end=-1)
	for i, p in enumerate(paragraph):
		if p in keyword_to_idx:
			keyword_idx = keyword_to_idx[p]
			if keyword_idx == 0:
				shortest_subarray_length[keyword_idx] = 1
			elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
				distance_to_previous_keyword = (
					i - latest_occurrence[keyword_idx - 1])
				shortest_subarray_length[keyword_idx] = (
					distance_to_previous_keyword + 
					shortest_subarray_length[keyword_idx - 1])

			latest_occurrence[keyword_idx] = i

			if (keyword_idx == len(keywords) - 1
					and shortest_subarray_length[-1] < shortest_distance):
				shortest_distance = shortest_subarray_length[-1]
				result = Subarray(start=i - shortest_distance + 1, end=i)
	return result



paragraph = """
A A x x B x x B C A
D x C D x x A C D x
C A x x B C x x D x
D B C A B D x C B x
""".split()

keywords = ['A', 'B', 'C', 'D']


print(find_smallest_sequentially_covering_subset_n2(paragraph, keywords))
print(find_smallest_sequentially_covering_subset(paragraph, keywords))

