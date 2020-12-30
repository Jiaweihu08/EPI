"""
Given a letter and a magazine, determine whether it is possible
to construct the letter with the characters in the magazine
"""
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
	char_count_from_letter = collections.Counter(letter_text)
	for c in magazine_text:
		if c in char_count_from_letter:
			char_count_from_letter[c] -= 1
			if char_count_from_letter[c] == 0:
				del char_count_from_letter[c]
				if not char_count_from_letter:
					return True
	return not char_count_from_letter


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
	return (not collections.Counter(letter_text) - 
		collections.Counter(magazine_text))

