"""
Define a function that takes two integers x and y as inputs
and return the result of x ** y

The naive approach is to use a recursion to compute x ** (y - 1)
and multiply that result with x.

x ** (a + b) = x ** a + x ** b

double the exponential of x at each iteration looping through
the bits of y and only multiply the resulting x to the result
when a 1-bit is accountered
"""

def pow_naive(x, y):
	if y == 0:
		return 1

	if y < 0:
		x, y = 1 / x, -y
	
	return x * pow(x, y - 1)


def pow(x, y):
	result, power = 1.0, y

	if y < 0:
		x, power = 1 / x, -power

	while power:
		if power & 1:
			result *= x
		x, power = x * x, power >> 1

	return result

print(pow(1/3, -2))

