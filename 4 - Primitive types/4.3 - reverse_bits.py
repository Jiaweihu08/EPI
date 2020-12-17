def reverse_bits_brute_force(x):
	"""
	swap the bits of the first half with the ones of the second half
	"""
	def swap_bits(x, i, j):
		if (x >> i) & 1 != (x >> j) & 1:
			bit_mask = (1 << i) | (1 << j)
			x ^= bit_mask
		return x

	for i in range(32):
		j = 63 - i
		x = swap_bits(x, i, j)
	return x

print(reverse_bits_brute_force(0))


# PRECOMPUTED_REVERSE = {}
# def reverse_bits(x):
# 	mask_size = 16
# 	bit_mask = 0xFFFF
# 	return PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size) |
# 		PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2 * mask_size) |
# 		PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << masi_size |
# 		PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask]