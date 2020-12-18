def swap_bits(x, i, j):
	"""
	Compare the values of x at i and j if they differ,
	flip their values by using a mask and the bitwise
	XOR operator. 

	1 = 00...001
	1 << 2 = 00...100
	1 << 3 = 00...1000
	1 << 1 | 1 << 2 = 00...0110 = 4 + 2 = 6
	"""
	if (x >> i) & 1 != (x >> j) & 1:
		bit_mask = (1 << i) | (1 << j)
		x ^= bit_mask
	return x