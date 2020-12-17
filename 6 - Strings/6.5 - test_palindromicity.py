def is_palindrome(s):
	i, j = 0, len(s) - 1
	while i <= j:
		while not s[i].isalnum():
			i += 1
		while not s[j].isalnum():
			j -= 1

		if s[i].lower() != s[j].lower():
			return False

		i, j = i + 1, j - 1
	return True


def is_palindrome_pythonic(s):
	return all(
		a == b
		for a, b in zip(
			map(str.lower, filter(str.isalnum, s)),
			map(str.lower, filter(str.isalnum, reversed(s)))
			)
		)

s1 = 'A man, a plan, a canal, Panama'
s2 = 'Able was I, ere I saw Elba!'
s3 = 'Ray a Ray'

for s in (s1, s2, s3):
	print(is_palindrome_pythonic(s))

	