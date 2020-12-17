# import math
import string
import functools


def int_to_str(x):
	# result = []
	# l = 0
	# if num < 0:
	# 	result.append('-')
	# 	l = 1
	# 	num = -num
	# num_digits = math.floor(math.log10(num)) + 1
	
	# for _ in range(num_digits):
	# 	num_digits -= 1
	# 	result.append(str(num // (10 ** num_digits)))
	# 	num %= 10 ** num_digits
	# return ''.join(result)

	is_negative = False
	if x < 0:
		x, is_negative = -x, True

	s = []
	while True:
		s.append(chr(ord('0') + x % 10))
		x //= 10
		if x == 0:
			break

	return ('-' if is_negative else '') + ''.join(reversed(s))


def str_to_int(s):
	# result = 0
	# sign = 1
	# l = 0
	# if num[0] in ('-', '+'):
	# 	if num[0] == '-':
	# 		sign = -1
	# 	l = 1
	
	# n = len(num[l:])
	# for i in range(n):
	# 	result += int(num[l:][i]) * (10 ** (n - 1 - i))
	# return result * sign

	return (-1 if s[0] == '-' else 1) * functools.reduce(
		lambda running_sum, c: running_sum * 10 + string.digits.index(c),
		s[s[0] in '-+':], 0)


print(str_to_int('-301'))



