"""
Given an array of words and a set of keywords, find the smallest subset from
array that contains all keywords
"""
def find_smallest_subarray_covering_set_n3(paragrah, keywords):
	"""
	Compute all possible subarrays of size from range(len(keywords), len(paragrah))
	and find see if they contain all the keywords

	O(n^3) time complexity
	"""
	min_size = len(paragrah)
	result = None
	for subarray_size in range(len(keywords), len(paragraph)):
		for i in range(len(paragraph) - subarray_size):
			remaining_keywords = keywords.copy()
			start = -1
			for j, word in enumerate(paragraph[i: i + subarray_size]):
				if not remaining_keywords:
					if i + j - 1 - start < min_size:
						min_size = i + j - 1 - start
						result = (start, i + j - 1)
						break

				if word in remaining_keywords:
					remaining_keywords.remove(word)
					if start == -1:
						start = i + j

	return result


def find_smallest_subarray_covering_set_n2(paragrah, keywords):
	"""
	For each position i, we grow the subarray incrementally and stop
	as soon as all keywords are found and store the start and end of
	the subarray

	Return the subarray that has the smallest (end - start)

	O(n^2) time complexity
	"""
	min_size = len(paragrah)
	result = None
	for i in range(len(paragraph)):
		remaining_keywords = keywords.copy()
		start = -1
		for j, word in enumerate(paragraph[i:]):
			if not remaining_keywords:
				if i + j - 1 - start < min_size:
					min_size = i + j - 1 - start
					result = (start, i + j - 1)
				break
			
			if word in remaining_keywords:
				remaining_keywords.remove(word)
				if start == -1:
					start = i + j
				
	return result


def find_smallest_subarray_covering_set(paragrah, keywords):




paragraph = """the the x x x x x or x x 
x x for and x x the for and x
for the x x and or for x x x 
for x and the x x x for or x""".split()

keywords = set(['the', 'or', 'and', 'for'])
# print(find_smallest_subarray_covering_set_n3(paragraph, keywords))
# print(find_smallest_subarray_covering_set_n2(paragraph, keywords))

