"""
Generate the powersets of a list of unique elements.
{0,1,2} --> {{},{0},{1},{2},{0,1},{0,2},{1,2},{0,1,2}}
"""
def compute_power_set(input_set):
	"""
	Buil power sets incrementally from the power sets of smaller size
	
	The power set of size 3 it built on that of size 2, and this is
	in turn built on the power set of size 1.

	input: [0, 1, 2]
	
	power set of size 1: {{2}, {}}
	
	build the power set of size 2. Add element 1 to all components of the
	previous power set: {{1}, {1,2}} + {{2}, {}} = {{1}, {1, 2}, {2}, {}}
	
	build the power set of size 3: {{},{0},{1},{2},{0,1},{0,2},{1,2},{0,1,2}}
	"""
	def compute_power_start_at(i):
		if len(input_set[i:]) == 1:
			return [input_set[i:], []]
		sub_power_set = compute_power_start_at(i + 1)
		return [[input_set[i]] + sub for sub in sub_power_set] + sub_power_set	
	return [[]] if not input_set else compute_power_start_at(0)
	
	# Without using recursion
	
	# if not input_set:
	# 	return [[]]
	# result = [[input_set[0]], []]
	# for i in range(1, len(input_set)):
	# 	result.extend([[input_set[i]] + subset for subset in result])
	# return result


def generate_power_set(input_set):
	def directed_power_set(to_be_selected, selected_so_far):
		if to_be_selected == len(input_set):
			power_sets.append(selected_so_far)
			return
		directed_power_set(to_be_selected + 1, selected_so_far)
		directed_power_set(to_be_selected + 1,
			selected_so_far + [input_set[to_be_selected]])
	power_sets = []
	directed_power_set(0, [])
	return power_sets


print(generate_power_set([0,1,2]))
