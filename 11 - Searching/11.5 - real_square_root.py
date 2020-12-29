"""
Given a float, compute its sqrt
"""
import math


def square_root(x):
	left, right = (x, 1.0) if x < 1.0 else (1.0, x)

	while not math.isclose(left, right):
		mid = (left + right) / 2
		mid_squared = mid * mid
		if mid_squared <= x:
			left = mid
		else:
			right = mid
	return left


print(square_root(81))