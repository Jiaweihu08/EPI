"""
Given a string that encodes an integer number in base1,
return its representation in a different base base2

Strategy:
Conver the number from base1 to decimal, then convert the
decimal number in base2

-------

string.digits / string.hexdigits can be used to convert
integers to strings without using str()

string.digits.index() / string.hexdigits.index() can be
used to map strings to integers without using int()

Decimal integer x to x in base b:

	result = ''
	while x:
		result = string.hexdigits[x % base].upper() + result
		x //= base
	return result

Integer in base != 10 to decimal:
	Multiply the each digit with the base ** i, where i is its
	index counted in reverse order then sum the products
	617 in base 7 == 6 * 7 ** 2 + 1 * 7 ** 1 + 7 * 7 ** 0

	functools.reduce can be used to simplify the code

"""
import functools, string


def convert_base(num_as_string, b1, b2):
	def construct_from_base(num_as_int, base):
		return ('' if num_as_int == 0 else
			construct_from_base(num_as_int // base, base) + 
			string.hexdigits[num_as_int % base].upper())

	is_negative = (num_as_string[0] == '-')
	num_as_int = functools.reduce(
		lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
		num_as_string[is_negative:], 0)

	return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
		construct_from_base(num_as_int, b2))


print(convert_base('615', 7, 13))

