"""
&: bitwise AND
|: bitwise OR
^: bitwise XOR
~: 1's complementary
>>: right shift operator
<<: left shift operator

x & 1, checks if the least significant bit of x is 1
x >>= 1, erase the rightmost bit from x
"""

def parity_count_bits(x):
	'''
	counts how many bits are there
	'''
	result = 0
	while x:
		result += x & 1
		x >>= 1

	return 0 if result % 2 == 0 else 1


def parity_mod_2(x):
	'''
	^ is used here to perform mod 2.
	i ^ j returns 1 if the leftmost bit from i and j
	are either (1,0) of (0,1)

	result starts at 0 and it would change its value to 1
	or later from 1 to 0 every time a bit = 1 is encountered

	'''
	result = 0
	while x:
		result ^= x & 1
		x >>= 1

	return result


def parity_remove_lowest_bit(x):
	'''
	x & (x - 1) returns x with its lowest set bit removed
	e.g. x = 16 -> 10000, 16&(16-1) = 00000
	x = 15 -> 1111, 15&(15-1) = 1110
	we can take advantage of this property and update the result
	at each iteration
	'''
	result = 0
	while x:
		result ^= 1
		x &= x - 1
	return result


# PRECOMPUTED_PARITY = {}
# def parity_cache(x):
# 	"""
# 	PRECOMPUTED_PARITY is a lookup table that stores the parity of
# 	all possible combinations of 16-bits integers.

# 	Our inputs are 64-bits integers and we split them into 4, 16-bits
# 	integers and compute their parities, our final parity is then the
# 	parity of these 4 values.

# 	To achieve this, we first need to extract the 4 groups of 16 bits
# 	from the initial input integer, with corresponding indexes of
# 	63-48, 47-32, 31-16, 15-0.
	
# 	For the first group, x >> (3 * 16) would do the trick, but to
# 	extract the second one, however, x >> (2 * 16) woud give us the
# 	bits from range 63-32. We can use the bitwise AND operator for the
# 	obtained bits and a number that represents 16 consecutive 1's in
# 	binary to extract the last 16 bits. The same is for the remaining
# 	two groups
# 	"""
# 	mask_size = 16
# 	bit_mask = x0FFF # = 111111...1 in total 16 set bits
# 	return PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
# 			PRECOMPUTED_PARITY[(x >> (2 * mask_size)) & bit_mask] ^
# 			PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask] ^
# 			PRECOMPUTED_PARITY[x & bit_mask]


def parity_xor(x):
	"""
	At each step we compute XOR for the first and second half of
	the result obtained from the last step:
	parity(11010111) = parity(XOR(1101, 0111)) = parity(XOR(10, 10))
	= parity(XOR(0, 0)) = parity(0) = 0 & 1

	For that we need to extract the first and the second half of
	entire bits from the last step, however, by computing XOR for x
	and the second half of the same x we achieve the same result
	since we compute x & 1 before returning the output. 1 here is used
	as a mask
	"""
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1
	return x & 1


print(parity_xor(3))




