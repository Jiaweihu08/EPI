"""
Given a sequence of stars, return a list of k closest stars
"""


import math
import heapq


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
	for star in stars:
		heapq.heappush(min_heap, (-star.distance, star))
		if len(max_heap) == k + 1:
			heapq.heappop(max_heap)
	return [s[1] for s in heapq.nlargest(k, max_heap)]