"""
Given a string and test whether it can be permuted to be palindromic
"""
import collections


def palindromic_perm(s):
	return sum(v % 2 for v in collections.Counter(s).values()) <= 1


print(palindromic_perm('rotator'))
