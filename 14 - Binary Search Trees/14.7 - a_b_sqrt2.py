"""
Design an algorithm for efficiently computing the k smallest numbers
of the form a + b * srqt(2) for nonnegative integers a and b.
"""
import heapq, math


class Number:
	def __init__(self, a, b):
		self.a, self.b = a, b
		
	def __lt__(self, other):
		return self.val < other.val

	def __eq__(self, other):
		return self.val == other.val

	@property
	def val(self):
		return self.a + self.b * math.sqrt(2)


def generate_first_k_a_b_sqrt2(k):
	candidates = [Number(0, 0)]
	seen = set()
	result = []
	while len(result) < k:
		next_smallest = heapq.heappop(candidates)
		result.append(next_smallest.val)
		increment_a = Number(next_smallest.a + 1, next_smallest.b)
		increment_b = Number(next_smallest.a, next_smallest.b + 1)
		if increment_a.val not in seen:
			seen.add(increment_a.val)
			heapq.heappush(candidates, increment_a)
		if increment_b.val not in seen:
			seen.add(increment_b.val)
			heapq.heappush(candidates, increment_b)
	return result


print(generate_first_k_a_b_sqrt2(20))

