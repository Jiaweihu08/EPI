def count_bits_naive(x):
	"""
	x is a 64-bits integer, so the number of iterations here
	is 64.
	for each bit from the right, we check if it's 1 and then
	remove it.
	"""
	num_bits = 0
	while x:
		num_bits += x & 1
		x >>= 1

	return num_bits


def count_bits_wegner(x):
	"""
	x & (x - 1) returns x with its last set bit removed
	so if the input integer is 1000....0 then the number
	of iterations will be 1 instead of 64, which is the case
	of the naive approach
	"""
	num_bits = 0
	while x:
		num_bits += 1
		x &= x - 1
	return num_bits


print(count_bits_wegner(1))