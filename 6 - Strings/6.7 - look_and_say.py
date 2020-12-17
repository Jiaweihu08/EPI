import itertools


def look_and_say(n):
	"""
	Generate n numbers from the previous one
	
	At each iteration, compare the current number with the previous
	one and act accordingly
	"""
	def next_number(s):
		result = []
		prev = s[0]
		count = 0
		for char in s:
			if char == prev:
				count += 1
			else:
				result.append(str(count) + prev)
				prev = char
				count = 1

		result.append(str(count) + prev)
		return ''.join(result)

	if n == 0:
		return '1'

	s = '1'
	for _ in range(1, n):
		s = next_number(s)

	return ''.join(s)


def look_and_say_2(n):
	"""
	Instead of looking back, look forward for comparison
	"""
	def next_number(s):
		result, i = [], 0
		while i < len(s):
			count = 1
			while i + 1 < len(s) and s[i] == s[i + 1]:
				count += 1
				i += 1
			result.append(str(count) + s[i])
			i += 1
		return ''.join(result)

	s = '1'
	for _ in range(1, n):
		s = next_number(s)
	return s


def look_and_say_pythonic(n):
	s = '1'
	for _ in range(1, n):
		s = ''.join(
			[str(len(list(group))) + key for key, group in itertools.groupby(s)])
	return s
print(look_and_say_pythonic(9))




