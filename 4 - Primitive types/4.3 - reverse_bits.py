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


PRECOMPUTED_REVERSE = {}
def reverse_bits(x):
	"""
	PRECOMPUTED_REVERSE is a hash table that contains the reverse values
	for all possible 16-bits integers

	And the bit_mask here is the corresponding value in decimal of 16
	consecutive 1's in binary.
	
	Since the input integer is 64-bits, bit_mask can be used to retrieve
	the different parts of x that are 16-bits long. We can then reverse these
	parts and place them in their correct positions to reverse x in binary

	e.g. say that we have an 8-bits input (10110110), and we use a 2-bits mask
	to retrieve the 4 following parts of the input: 10, 11, 01, 10. The reversed
	version of the input is them composed of the reversed version of these 4 parts
	in an reversed order: 01 10 11 01

	x & bit_mask will retrive the first 16 digits from the binary representation
	then we can use the push left operator to move it to its correct position

	The bitwise OR operator is used to combine the resulting reversed versions of
	these 4 parts

	"""
	mask_size = 16
	bit_mask = 0xFFFF
	return PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size) |
		PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2 * mask_size) |
		PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << masi_size |
		PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask]


		