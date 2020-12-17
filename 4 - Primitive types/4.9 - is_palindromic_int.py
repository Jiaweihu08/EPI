import math

def is_palindromic_brute_force(x):
	x = str(x) # Time complexity O(n^2)?
	for i in range(len(x) // 2):
		if x[i] != x[-i-1]:
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
# print(is_palindromic_brute_force(1))