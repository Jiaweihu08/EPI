"""
Given a list of coins represented by an array of integers. Find
the maximum revenue of the pick-up-coins game for the starting
player if one can only pick coins from either left or right
extreme of the array. Players cannot skip turns.
"""
import functools


def maximum_revenue(coins):
	@functools.lru_cache(None)
	def compute_maximum_revenue_for_range(a, b):
		if a > b:
			return 0

		max_revenue_a = coins[a] + min(
			compute_maximum_revenue_for_range(a + 2, b),
			compute_maximum_revenue_for_range(a + 1, b - 1))

		max_revenue_b = coins[b] + min(
			compute_maximum_revenue_for_range(a + 1, b - 1),
			compute_maximum_revenue_for_range(a, b - 2))
		return max(max_revenue_a, max_revenue_b)
	return compute_maximum_revenue_for_range(0, len(coins) - 1)


coins = [10,25,5,1,10,5]
print(maximum_revenue(coins))