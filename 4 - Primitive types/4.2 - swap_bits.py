def swap_bits(x, i, j):
	"""
	Compare the values of x at i and j and if they differ, we flip
	their values by using a mask and the bitwise XOR operation
	"""
	if (x >> i) & 1 != (x >> j) & 1:
		bit_mask = (1 << i) | (1 << j)
		x ^= bit_mask
	return x