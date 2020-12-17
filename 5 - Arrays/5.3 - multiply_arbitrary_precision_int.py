# import math


# def multiply_naive(num1, num2):
# 	prod = int(''.join(map(str, num1))) * int(''.join(map(str,num2)))
# 	sign = 1 if prod > 0 else -1
# 	prod = abs(prod)

# 	num_digits = math.floor(math.log10(prod)) + 1
# 	result = [0] * num_digits
# 	for i in reversed(range(num_digits)):
# 		result[i] = prod % 10
# 		prod //= 10

# 	result[0] *= sign
# 	return result


# print(multiply_naive([-1,2,3], [2,3]))


def multiply(num1, num2):
	"""
	^: bitwise XOR
	"""
	sign = -1 if (num1[0] < 0) ^ (num2[0]) else 1
	num1[0], num2[0] = abs(num1[0]), abs(num2[0])

	result = [0] * (len(num1) + len(num2))
	for i in reversed(range(len(num1))):
		for j in reversed(range(len(num2))):
			result[i + j + 1] += num1[i] * num2[j]
			result[i + j] += result[i + j + 1] // 10
			result[i + j + 1] %= 10

	result = result[next((i for i, x in enumerate(result)
		if x != 0), len(result)):] or [0]

	return [sign * result[0]] + result[1:]


print(multiply([-1,2,3], [2,3]))

