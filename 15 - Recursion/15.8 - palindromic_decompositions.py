"""
Given a string, find all of its palindromic decompositions
"""
def palindromic_decomposition(text):
	def directed_palindromic_decomposition(offset, partial_partition):
		if offset == len(text):
			result.append(partial_partition.copy())
			return

		for i in range(offset + 1, len(text) + 1):
			prefix = text[offset:i]
			if prefix == prefix[::-1]:
				directed_palindromic_decomposition(
					i, partial_partition + [prefix])
	result = []
	directed_palindromic_decomposition(0, [])
	return result


print(palindromic_decomposition('0204451881'))
