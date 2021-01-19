import functools


# def roman_to_decimal(s):
# 	T = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	
# 	result = 0
# 	for i in range(len(s) - 1):
# 		result += T[s[i]] if T[s[i]] >= T[s[i + 1]] else -T[s[i]]
# 	result += T[s[-1]]
# 	return result


def roman_to_decimal_pythonic(s):
	T = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

	return functools.reduce(
		lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
		range(len(s) - 1), T[s[-1]])


def integer_to_roman(n):
	T = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90:"XC", 50: "L",
		40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

	if n in T.keys():
		return T[n]

	result = ''
	for k in T.keys():
		while n >= k:
			result += T[k]
			n -= k
	return result	