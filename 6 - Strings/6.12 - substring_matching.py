"""
Given two strings s and t, find the starting position of s in t if
s is a substring of t, otherwise return -1.

The naive approach is to go through t and at each position i compare
the substring starting at i to s. This leads to a O(n^2) algorithm.

A simple and more efficient algorithm for string matching is the
Rabin-Karp algorithm. This algorithm relies on the concept of fingeprint
which is a rolling hash of the strings. Using this hash function, the
hashes of sliding windows of t can be computed very efficiently.
"""
import functools


def rabin_karp(s, t):
	if len(s) > len(t):
		return -1

	base = 26
	t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
	s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
	power_s = base ** max(len(s) - 1, 0)

	for i in range(len(s), len(t)):
		if t_hash == s_hash and t[i - len(s):i] == s:
			return i - len(s)

		t_hash -= ord(t[i - len(s)]) * power_s
		t_hash = t_hash * base + ord(t[i])

	if t_hash == s_hash and t[-len(s):] == s:
		return len(t) - len(s)
	return -1