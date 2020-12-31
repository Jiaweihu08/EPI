"""
Given an array of words and a set of keywords, find the smallest subset from
array that contains all keywords
"""
import collections


def find_smallest_subarray_covering_set_n3(paragrah, keywords):
	"""
	Compute all possible subarrays of size from range(len(keywords), len(paragrah))
	and see if they contain all the keywords
	
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


Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
	"""
	A crucial fact to realize when trying to improve from the O(n^2)
	solution is that, when growing a given subarray we start from a
	given index i and stop at j when all words are covered, there is
	not point to consider a the subarray that starts at i + 1 and ends
	before j. At j we found the last keyword from the set, and before
	that not even the array from i to j covers the set, let alone a
	subarray

	Having realized that, we can improve the runtime to O(n) doing the
	following. Grow the subarray incrementally until all words from
	set are covered. Now advance i until the set is not covered anymore.
	This means that one of the words from the set is now on the left
	side of i, and we need to keep advancing j to find the next word
	that's just being left out by advancing i. On our way finding the
	next word i just passed by we may encounter other words from the set,
	but we won't stop by since the set is not covered until the word
	being just left out is found again

	Once that is done, we will keep advancing i until another word being
	left out make the subarray no longer covers the set, and the process
	is repeated until j reaches the end of the array

	e.g.
	Array of words:
	['apple','banana','dog','banana','dog','cat','apple','dog','banana','apple','cat','dog']

	Set of keywords:
	['banana','cat','dog']

	First the subarray with all keywords is found from i=0, j=5:
	['apple','banana','dog','banana','dog','cat']
	But there is an even smaller one with i=3 ending with the same j:
	['banana','dog','cat']

	The next candidate subarray to consider is the one from i=4 j=8:
	since with i=4, j=5 we just left 'banana' out, and j=8 in the array
	is 'banana'

	Advancing i to 5 we leave 'dog' out and j is advanced to 11 to find
	it again.
	[cat','apple','dog','banana','apple','cat','dog']

	The last set to be considere is the following:
	['banana','apple','cat','dog']
	"""
	keywords_to_cover = collections.Counter(keywords)
	result = Subarray(start=-1, end=-1)
	remaining_keywords = len(keywords)
	left = 0
	for right, p in enumerate(paragraph):
		# when a keyword is found, we reduce its count by one.
		# remaining_keywords is reduce only once per keyword when
		# advancing right
		if p in keywords:
			keywords_to_cover[p] -= 1
			if keywords_to_cover[p] >= 0:
				remaining_keywords -= 1

		# remainig_keywords = 0 means that all keywords are found in
		# the subarray defined by paragraph[left, right + 1], we now
		# proceed to reduce the size of the subarray until it no longer
		# covers all keywords
		while remaining_keywords == 0:
			# update the subarray if needed
			if (result == Subarray(start=-1, end=-1)
					or right - left < result.end - result.start):
				result = Subarray(start=left, end=right)
			pl = paragraph[left]

			# if the word being left out in the current step is a
			# keyword, we increment its count. There can be more than
			# one of this word in the subarray so we only increment
			# remaining_keywords when this is the last one i.e. its
			# count is > 1
			if pl in keywords:
				keywords_to_cover[pl] += 1
				if keywords_to_cover[pl] > 0:
					remaining_keywords += 1
			left += 1
	return result


def find_smallest_subarray_covering_set_linkedlist(paragraph, keywords):
	"""
	Iterate over the array and entries that are keywords are stored in a
	doubly linked list, using their indices at values. The indices are
	stored in order and each time an entry that's already in the list is
	encountered the old one is removed and the new one is inserted to the
	end of the list

	When the size of the list reaches that of the keywords, the the size
	of the subarray is computed and the smallest one is returned at the end
	"""
	class DoublyLinkedListNode:
		def __init__(self, data=None):
			self.data = data
			self.prev = self.next = None

	class LinkedList:
		def __init__(self):
			self.head = self.tail = None
			self._size = 0

		def __len__(self):
			return self._size

		def insert_after(self, value):
			node = DoublyLinkedListNode(value)
			node.prev = self.tail
			if self.tail:
				self.tail.next = node
			else:
				self.head = node
			self.tail = node
			self._size += 1

		def remove(self, node):
			if node.next:
				node.next.prev = node.prev
			else:
				self.tail = node.prev
			if node.prev:
				node.prev.next = node.next
			else:
				self.head = node.next
			node.prev = node.next = None
			self._size -= 1

	loc = LinkedList()
	d = {s: None for s in keywords}
	result = Subarray(start=-1, end=-1)
	for idx, s in enumerate(paragraph):
		if s in d:
			it = d[s]
			if it is not None:
				loc.remove(it)
			loc.insert_after(idx)
			d[s] = loc.tail

			if len(loc) == len(keywords):
				if (result == Subarray(start=-1, end=-1)
					or idx - loc.head.data < result.end - result.start):
					result = Subarray(start=loc.head.data, end=idx)
	return result


paragraph = """the the x x x x x or x x 
x x for and x x the for and x
for the x x and or for x x x 
for x and the x x x for or x""".split()

keywords = set(['the', 'or', 'and', 'for'])

print(find_smallest_subarray_covering_set_n3(paragraph, keywords))
print(find_smallest_subarray_covering_set_n2(paragraph, keywords))
print(find_smallest_subarray_covering_set(paragraph, keywords))
print(find_smallest_subarray_covering_set_linkedlist(paragraph, keywords))

