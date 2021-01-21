"""
Test if a string s is palindromic.
"""
def is_palindromic(s):
	return all(s[i] == s[~i] for i in range(len(s) // 2))
