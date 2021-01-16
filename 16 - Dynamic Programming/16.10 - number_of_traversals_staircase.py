"""
Given an integer n representing the number of stairs to climb,
and k the number of maximum number of steps you can take each
time. Return the number of different ways to climb the n stairs.
"""
import functools


def number_of_moves_to_climb_stairs(top, maximum_step):
	@functools.lru_cache(None)
	def compute_number_of_ways_to_h(h):
		if h <= 1:
			return 1

		return sum(
			compute_number_of_ways_to_h(h - i)
			for i in range(1, min(h, maximum_step) + 1))
	return compute_number_of_ways_to_h(top)


print(number_of_moves_to_climb_stairs(4, 2))