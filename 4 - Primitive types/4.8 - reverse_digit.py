# def reverse_digit_brute_force(num):
# 	num = str(num)
# 	left, right = '', ''
# 	for i in range((len(num) + 1) // 2):
# 		right = num[i] + right
# 		left += num[-i-1]

# 	if len(num) % 2 != 0:
# 		left = left[:-1]

# 	return int(left+right)

# print(reverse_digit_brute_force(314))

def reverse_digit(x):
	"""
	The most important thing to realize here is how to get the
	least significant digt from the given number.
	i.e.
		last_digit = x % 10
		x //= 10
	"""
	result, x_remain = 0, abs(x)
	while x_remain:
		result = result * 10 + x_remain % 10
		x_remain //= 10
	return -result if x < 0 else result

print(reverse_digit(314))