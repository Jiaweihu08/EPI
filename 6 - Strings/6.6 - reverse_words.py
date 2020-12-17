def reverse_words_naive(s):
	"""
	Not inplace
	O(n) time and space complexity
	"""
	return ' '.join(reversed(s.split()))


def reverse_words(s):
	def reverse_range(start, end):
		while start < end:
			s[start], s[end] = s[end], s[start]
			start, end = start + 1, end - 1

	reverse_range(0, len(s) - 1)

	start = 0
	while True:
		end = start
		while end < len(s) and s[end] != ' ':
			end += 1
		reverse_range(start, end - 1)
		start = end + 1
		if end == len(s):
			break
	print(''.join(s))

s = 'Alice like Bob'
reverse_words([i for i in s])
