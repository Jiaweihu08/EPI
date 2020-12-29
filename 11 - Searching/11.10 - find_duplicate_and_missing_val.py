"""
Given a list A of n - 1 integers from range [0, n - 1], both inclusive,
The XOR operation for values in the list and the range will give us
the value that's missing in A

Properties of XOR:

x ^ 0 = x
x ^ x = 0

e.g. A = [0,1,2,3]
	range [0, n - 1] = [0,1,2,3,4]

(XOR for values from A) XOR (XOR for values from range [0, n - 1])
= (0 ^ 1 ^ 2 ^ 3) ^ (0 ^ 1 ^ 2 ^ 3 ^ 4)
= (0 ^ 0) ^ (1 ^ 1) ^ (2 ^ 2) ^ (3 ^ 3) ^ 4
= 0 ^ 0 ^ 0 ^ 0 ^ 4
= 4

Now consider the case where the list A that's given contains values from
range [0, n - 1] but one value m is missing and a value t has been entered
twice, how can we find these two values?

Computing (XOR for range) XOR (XOR for A) will give us (m XOR t), since
the missing value m has only been XORed once and the duplicate value t has
been XORed tree times, all other values are XORed twice, thus cancelled to
zero. e.g. m ^ m ^ m ^ t = m ^ t

Since m is not t, m ^ t always has a bit set, and this bit has to come from
either m or t. There has to be an odd number of entries from range and A that
this bit is set, otherwise the XOR operation at the begining would have unset
the bit, which means that if we compute the XOR for these values, the result
has to be either m or t

A = [0,1,2,3,3]   =   [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,1)]
range = [0,1,2,3,4] = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0)]

m ^ t = (1,1,1), we choose the rightmost set bit(could be any of set bit) and
compute XOR for all entries from range and A that have this bit set:

A -> [1,3,3], range -> [1,3]

1 ^ 3 ^ 3 ^ 1 ^ 3 = 3 = m or t
"""
import collections
import functools


DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
	('duplicate', 'missing'))


def find_duplicate_missing(A):
	# compute XOR for values from [0, n - 1] and A
	# m ^ t
	miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A),
		0)

	# differ_bit is the LSB from miss_xor_dup
	# x &= (x - 1) removes the LSB from x because 
	# x and x - 1 differ in x's LSB and possibly beyond
	# ~(x - 1) and x are the same only at x's LSB and possibly beyond
	differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
	# compute XOR for entries that has the differ_bit set
	for i, a in enumerate(A):
		if i & differ_bit:
			miss_or_dup ^= i
		if a & differ_bit:
			miss_or_dup ^= a

	# (t, t ^ m ^ t) or (m, m ^ m ^ t)
	return (DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_xor_dup)
		if miss_or_dup in A else
		DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup))


A = [0,1,2,2,3,5]
print(*find_duplicate_missing(A))

