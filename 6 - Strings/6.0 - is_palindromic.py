"""
Test if a string s is palindromic
"""


def is_palindromic(s):
	"""
	Compare entries inwards and return False if there is
	any mismatch
	"""
	return all(s[i] == s[~i] for i in range(len(s) // 2))

print(is_palindromic('palindrom'))