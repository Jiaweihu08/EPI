"""
Implement a Stack that, other than push and pop, also has keeps track
of the max element contained in the stack
"""
import collections


class Stack_1:
	def __init__(self):
		self.values = []

	def push(self, value):
		"""
		O(1) time and space complexity
		"""
		self.values.append(value)

	def pop(self):
		"""
		O(1) time and space complexity
		"""
		return self.values.pop()

	def max(self):
		"""
		O(n) time complexity
		"""
		# largest = float('-inf')
		# for num in self.values:
		# 	if num > largets:
		# 		largets = num
		# return largest
		return max(self.values)


class Stack_2:
	def __init__(self):
		self.values = []
		self._max = []

	def push(self, value):
		"""
		O(n) time complexity
		O(1) space complexity
		"""
		self.values.append(value)
		temp = []
		while self._max and self._max[-1] > value:
			temp.append(self._max.pop())
		self._max.append(value)
		while temp:
			self._max.append(temp.pop())

	def pop(self):
		"""
		O(n) time complexity
		O(1) space complexity
		"""
		to_remove = self.values.pop()
		temp = []
		while self._max:
			if self._max[-1] != to_remove:
				temp.append(self._max.pop())
			else:
				self._max.pop()
				while temp:
					self._max.append(temp.pop())
				return to_remove

	def max(self):
		"""
		O(1) time and space complexity
		"""
		if self.values:
			return self._max[-1]


class Stack:
	"""
	O(1) time complexity
	O(n) space complexity
	"""
	ElementWithCacheMax = collections.namedtuple('ElementWithCacheMax',
		('element', 'max'))

	def __init__(self):
		self._element_with_cache_max = []

	def is_empty(self):
		return len(self._element_with_cache_max) == 0

	def max(self):
		return self._element_with_cache_max[-1].max

	def pop(self):
		return self._element_with_cache_max.pop().element

	def push(self, x):
		self._element_with_cache_max.append(
			self.ElementWithCacheMax(
				x, x if self.is_empty() else max(x, self.max())))


s = Stack()
for num in [1,2,3,0,5,-3]:
	s.push(num)
	print(f'max in stack:{s.max()}')


