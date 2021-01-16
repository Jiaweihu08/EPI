"""
Consider the problem of printing out a string of words separated
by single blanks. Each line can contain no more than a fixed
number of characters k, if the words does not reache k, the
remaining spaces are fille with blancks.


Greedy algorithms are doomed.

Suppose we have achieved the optimum placement for the first i
words, it is crucial to realize that removing this last word
does not necessarily give us the optimum placement for the first
i - 1 words.

When adding a new word to an optimum placement, this new word can
either be in a new row, or proceed the last word in the same row.


The approach shown below first considers the case of the newly
added word in a row on its own, then iteratively add previous
words to the same row and compute the minimum messiness from all
considered placements.
"""
import typing


def minimum_messiness(words, line_length):
	num_remaining_blanks = line_length - len(words[0])
	min_messiness = ([num_remaining_blanks ** 2] +
					[typing.cast(int, float('inf'))] * (len(words) - 1))
	for i in range(1, len(words)):
		num_remaining_blanks = line_length - len(words[i])
		min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks ** 2
		for j in reversed(range(i)):
			num_remaining_blanks -= len(words[j]) + 1
			if num_remaining_blanks < 0:
				break
			first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
			current_line_messiness = num_remaining_blanks ** 2
			min_messiness[i] = min(min_messiness[i],
				first_j_messiness + current_line_messiness)
	return min_messiness[-1]



words = ['aaa', 'bbb', 'c', 'd', 'ee', 'ff', 'ggggggg']
line_length = 11
print(minimum_messiness(words, line_length))