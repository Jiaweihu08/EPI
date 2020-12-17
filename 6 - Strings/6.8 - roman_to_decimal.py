import functools


def roman_to_decimal(s):
	T = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	result = 0
	for i in range(len(s)):
		if i < len(s) - 1 and T[s[i]] < T[s[i + 1]]:
			result -= T[s[i]]
		else:
			result += T[s[i]]

	return result


def roman_to_decimal_pythonic(s):
	T = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	# return functools.reduce(
	# 	lambda val, i: val + (-T[s[i]] if i < len(s) - 1 and T[s[i]] < T[s[i + 1]] else T[s[i]]),
	# 	range(len(s)), 0)
	return functools.reduce(
		lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
		reversed(range(len(s) - 1)), T[s[-1]])

S = ['XXXIII', 'XXXIV', 'IX', 'CMLXXXV', 'LIX', 'LVIIII']

for s in S:
	print(roman_to_decimal_pythonic(s))