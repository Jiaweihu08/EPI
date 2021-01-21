import string
import functools


def int_to_str(x):
	is_negative = False
	if x < 0:
		x, is_negative = -x, True

	s = []
	while True:
		s.append(string.digits[x % 10])
		# s.append(chr(ord('0') + x % 10))
		x //= 10
		if x == 0:
			break
	return ('-' if is_negative else '') + ''.join(reversed(s))


def str_to_int(s):
	return (-1 if s[0] == '-' else 1) * functools.reduce(
		lambda running_sum, c: running_sum * 10 + string.digits.index(c),
		s[s[0] in '-+':], 0)


print(str_to_int('-301'))
print(int_to_str(0))
