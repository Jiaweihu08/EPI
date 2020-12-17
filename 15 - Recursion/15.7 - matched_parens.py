"""
Generate all possible valid combinations of n parens
n = 3:
	'((()))', '()(())', '(()())', '(())()', '()()()'

We cannot place a closing parens without having a corresponding
opening. In other words, the number of remaining openings has always
be equal or smaller than the number of remaining closing parens
"""

def compute_matched_parens(n):
	def solve_matched_parens(num_open_remain, num_close_remain, prefix):
		if num_open_remain == 0:
			result.append(prefix + ')' * num_close_remain)
			return

		if num_open_remain > 0:
			solve_matched_parens(num_open_remain-1, num_close_remain, prefix + '(')

		if num_open_remain < num_close_remain:
			solve_matched_parens(num_open_remain, num_close_remain - 1, prefix + ')')
	
	result = []
	solve_matched_parens(n, n, '')
	return result

print(compute_matched_parens(4))

