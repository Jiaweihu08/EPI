"""
Given an array of words with some duplicates, find the distance
between a closest pair of words of equal entries
"""
import typing


def dist_for_nearest_repeats(A):
	word_to_last_index = {}
	nearest_repeated_distance = float('inf')
	for i, word in enumerate(A):
		if word in word_to_last_index:
			distance_to_last_repeate = word_to_last_index[word]
			nearest_repeated_distance = min(nearest_repeated_distance,
											distance_to_last_repeate)
		word_to_last_index[word] = i
	# return (-1 if nearest_repeated_distance == float('inf')
	# 		else nearest_repeated_distance)
	return (typing.cast(int, nearest_repeated_distance))
			if nearest_repeated_distance != float('inf') else -1




A = ['All','word','and','no','play','makes','for',
	'no','work','no','fun','and','no','results']

print(dist_for_nearest_repeats(A))