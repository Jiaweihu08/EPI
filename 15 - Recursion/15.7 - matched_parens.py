"""
Generate all possible valid combinations of n parens.

n = 3:
	'((()))', '()(())', '(()())', '(())()', '()()()'

We cannot place a closing parens without having a corresponding opening.
In other words, the number of remaining openings has always be equal or
smaller than the number of remaining closing parens.
"""
def generate_balanced_parentheses(num_pairs):
	def complete_prefix(num_remaining_open, num_remaining_close, prefix):
		if num_remaining_open == 0:
			result.append(prefix + ')' * num_remaining_close)
			return

		if num_remaining_open > 0:
			complete_prefix(
				num_remaining_open - 1, num_remaining_close, prefix + '(')

		if num_remaining_open < num_remaining_close:
			complete_prefix(
				num_remaining_open, num_remaining_close - 1, prefix + ')')
	
	result = []
	complete_prefix(num_pairs, num_pairs, '')
	return result


print(generate_balanced_parentheses(3))
