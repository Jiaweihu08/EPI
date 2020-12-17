# def pow_brute_force(x, y):
# 	if y == 0:
# 		return 1
	
# 	if y == 1:
# 		return x

# 	if y < 0:
# 		x = 1 / x
# 		y = - y
	
# 	return x * pow(x, y - 1)


def pow(x, y):
	result, power = 1.0, y

	if y < 0:
		x, power = 1 / x, -power

	while power:
		if power & 1:
			result *= x
		x, power = x * x, power >> 1

	return result

print(pow(1/3, -2))

