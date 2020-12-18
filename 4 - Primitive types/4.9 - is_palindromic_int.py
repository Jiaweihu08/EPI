"""
Test if a decimal integer is palindromic

The naive approach is to convert the integer into a string
and compare their values going inwards. The space complexity
is O(n)

We can avoid the O(n) space complaxity by comparing the most
significant digit with the least significant one by using 
floor division and remainder

Say that x = 1710, 
the number of digits is 4 = math.floor(math.log10(x)) + 1,
we define the mask as 10 ** (num_digits - 1) = 1000
x // 1000 = 1 gives us the most significant digit
and x % 10 = 0 is the least significant digit

we then remove the most and least significant digit by performing
x %= mask
x //= 10

Since the number of digits are now 2 less that before, we update the
mask to mask //= 100
"""
import math


def is_palindromic_naive(x):
	x = str(x)
	for i in range(len(x) // 2):
		if x[i] != x[~i]:
			return False
	return True


def is_palindromic(x):
	"""
	Use floor division // to find the most significant digit
	Use % to find the least significant digit

	When using the floor division operator, the number of remaining digits
	is needed.

	The number of digits of a given number x can be found by
	using math.floor(math.log10(x)) + 1

	We use x // 10**(num_digits - 1) to get the most significant digit
	"""
	if x <= 0:
		return x == 0

	num_digits = math.floor(math.log10(x)) + 1
	msd_mask = 10**(num_digits - 1)
	for _ in range(num_digits // 2):
		if x // msd_mask != x % 10:
			return False
		x %= msd_mask # removing the first digit
		x //= 10 # removing the last digit
		msd_mask //= 100 # update the mask

	return True


print(is_palindromic(101))
# print(is_palindromic_naive(1010))


