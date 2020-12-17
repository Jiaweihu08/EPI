# def compute_power_set(nums):
# 	def power_set_helper(i):
# 		if len(nums[i:]) == 1:
# 			return [nums[i:]]

# 		power_set = power_set_helper(i+1)
		
# 		new_set = [[nums[i]]+sub for sub in power_set]
		
# 		power_set.extend(new_set)

# 		power_set.append([nums[i]])

# 		return power_set
	
# 	power_set = power_set_helper(0)
	
# 	power_set.append([])
	
# 	return power_set

# print(compute_power_set([0,1,2]))

def generate_power_set(input_set):
	def directed_power_set(to_be_selected, selected_so_far):
		if to_be_selected == len(input_set):
			power_set.append(selected_so_far)
			return

		directed_power_set(to_be_selected+1, selected_so_far)

		directed_power_set(to_be_selected+1, selected_so_far + [input_set[to_be_selected]])

	power_set = []
	directed_power_set(0, [])
	return power_set

print(generate_power_set([0,1,2,3]))



