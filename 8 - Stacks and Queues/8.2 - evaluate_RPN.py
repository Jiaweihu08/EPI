"""
Given an arithmetical expression in RPN, return the number that
the expression evaluates to

E.g. '3,4,+,2,*,1+' -> 15
"""
def evaluate_rpn(expression):
	partial_eval = []
	delimiter = ','
	operators = {'+': lambda y, x: x + y, '-': lambda y, x: x - y,
				'x': lambda y, x: x * y, '/': lambda y, x: x // y}
	
	for token in expression.split(delimiter):
		if token in operators:
			partial_eval.append(
				operators[token](partial_eval.pop(), partial_eval.pop()))
		else:
			partial_eval.append(int(token))
	return partial_eval[-1]



s = '3,4,+,2,x,1,+'
print(evaluate_rpn(s))

