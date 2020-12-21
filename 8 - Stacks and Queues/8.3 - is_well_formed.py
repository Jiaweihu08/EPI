"""
Given a string containing different types of brackets,
test whether these brackets are placed correctly
"""

def is_well_formed(s):
	left_chars, lookups = [], {'(': ')', '[': ']', '{': '}'}
	for c in s:
		if c in lookups:
			left_chars.append(c)
		elif not left_chars or lookups[left_chars.pop()] != c:
				return False
	return not left_chars



s = "(()[]){()}"
print(is_well_formed(s))

