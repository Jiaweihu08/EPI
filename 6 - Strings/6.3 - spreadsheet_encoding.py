"""
Convert spread sheet column id into integer ids.

e.g. 'A' -> 1, 'D' -> 4, 'ZZ' -> 7.2
"""
import functools


def decode_ss_col_id(col):
	return  functools.reduce(
		lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
