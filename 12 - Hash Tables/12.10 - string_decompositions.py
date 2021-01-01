"""
Given a string s and an array of words, return the starting indices of
all substrings from s that are concatenations of all strings in words
"""
import collections


def find_all_substrings(s, words):
	"""
	Time complexity O(Nnm)
	N = len(s)
	n = len(words)
	m = len(words[0])

	For each nm position i in s, check if the substring s[i:i+nm] is
	a concatenation of all string in words
	"""
	def match_all_words(start):
		curr_word_to_freq = collections.Counter()
		for i in range(start, start + unit_size * len(words), unit_size):
			curr_word = s[i:i + unit_size]
			it = word_to_freq[curr_word]
			if it == 0:
				return False
			curr_word_to_freq[curr_word] += 1
			if curr_word_to_freq[curr_word] > it:
				return False
		return True

	word_to_freq = collections.Counter(words)
	unit_size = len(words[0])
	return [
		i for i in range(len(s) - unit_size * len(words) + 1)
			if match_all_words(i)
	]


s = 'barfoothefoobarman'
words = ['foo','bar']
print(find_all_substrings(s, words))

