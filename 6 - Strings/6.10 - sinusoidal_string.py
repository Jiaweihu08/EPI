def make_sinusoidal_naive(s):
	top, middle, bottom = [], [], []
	for i in range(len(s)):
		if i % 2 == 0:
			middle.append(s[i])
		elif (i - 1) % 4 == 0:
			top.append(s[i])
		else:
			bottom.append(s[i])

	return ''.join(top+middle+bottom)


def make_sinusoidal(s):
	result = []
	for i in range(1, len(s), 4):
		result.append(s[i])

	for i in range(0, len(s), 2):
		result.append(s[i])

	for i in range(3, len(s), 4):
		result.append(s[i])

	return ''.join(result)


def make_sinusoidal_pythonic(s):
	return s[1::4] + s[::2] + s[3::4]


s = 'Hello World!'
print(make_sinusoidal_pythonic(s))