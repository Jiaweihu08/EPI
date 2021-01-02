"""
Given a sequence of stars, return a list of k closest stars

Use a max heap of size k, add stars to the heap as we iterate
through it and remove the one with the greatest distance at
each step

O(nlog(k)) Time complexity
O(log(k)) Space complexity
"""
import math
import heapq
import itertools


class Star:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	@property
	def distance(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def __lt__(self, other):
		return self.distance < other.distance


def find_closest_k_stars(stars, k):
	"""
	O(n) time complexity
	O(k) space complexity
	"""
	max_heap = []

	for star in itertools.islice(stars, k):
		heapq.heappush(max_heap, (-star.distance, star))

	for star in stars:
		heapq.heappushpop(max_heap, (-star.distance, star))

	return [s[1] for s in heapq.nlargest(k, max_heap)]


# Tested with EPIJudge
