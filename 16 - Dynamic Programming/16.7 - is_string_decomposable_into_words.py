"""
Given a string of characters and a set of dictionary words, determine
whether it is possible to decompose the string into dictionary words.
If it is, return the decomposition.
"""
# def all_string_dict_words_decompositions(domain, dictionary):
# 	def decompose_prefix_into_dict_words(i, sequence):
# 		for w in dictionary:
# 			if domain[i:i + len(w)] == w:
# 				if i + len(w) == len(domain):
# 					decompositions.append(sequence + [w])
# 				else:
# 					decompose_prefix_into_dict_words(
# 						i + len(w), sequence + [w])
# 	decompositions = []
# 	decompose_prefix_into_dict_words(0, [])
# 	return decompositions


def decompose_into_dictionary_words(domain, dictionary):
	last_length = [-1] * len(domain)
	for i in range(len(domain)):
		if domain[:i + 1] in dictionary:
			last_length[i] = i + 1
			continue

		for j in range(i):
			if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
				last_length[i] = i - j
				break

	decompositions = []
	if last_length[-1] != -1:
		idx = len(domain) - 1
		while idx >= 0:
			decompositions.append(domain[idx + 1 - last_length[idx]:idx + 1])
			idx -= last_length[idx]
		decompositions = decompositions[::-1]
	return decompositions



domain = 'amanaplanacanal'
dictionary = ['a', 'man', 'plan', 'canal']
print(decompose_into_dictionary_words(domain, dictionary))