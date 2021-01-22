def rl_encoding(s):
	# if not s:
	# 	return ''

	# result, count = [], 1
	# for i in range(len(s) - 1):
	# 	if s[i] == s[i + 1]:
	# 		count += 1
	# 	else:
	# 		result.append(str(count) + s[i])
	# 		count = 1
	# result.append(str(count) + s[-1])
	# return ''.join(result)

	result, count = [], 1
	for i in range(1, len(s) + 1):
		if i == len(s) or s[i] != s[i - 1]:
			result.append(str(count) + s[i - 1])
			count = 1
		else:
			count += 1
	return ''.join(result)


def rl_decoding(s):
	# result, i = [], 0
	# while i < len(s):
	# 	j = i
	# 	while j < len(s) - 1 and s[j].isdigit():
	# 		j += 1
	# 	result.append(s[j] * int(s[i:j]))
	# 	if j == len(s) - 1:
	# 		break
	# 	i = j + 1
	# return ''.join(result)
	
	result, count = [], 0
	for c in s:
		if c.isdigit():
			count = count * 10 + int(c)
		else:
			result.append(c * count)
			count = 0
	return ''.join(result)
