"""
Given a set of words, return groups of anagrams that have more than
two words
"""
import collections


def find_anagrams(words):
	sorted_string_to_anagrams = collections.defaultdict(list)
	for s in words:
		sorted_string_to_anagrams[''.join(sorted(s))].append(s)
	return [
		group for group in sorted_string_to_anagrams.values()
		if len(group) >= 2
	]


words = ['debitcard','badcredit','elvis','silent','lives','freedom','listen','levis','money']
print(find_anagrams(words))