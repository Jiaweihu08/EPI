def compute_valid_ip_addresses(s):
	def is_valid_part(s):
		return len(s) > 0 and (len(s) == 1 or (s[0] != '0' and int(s) <= 255))

	result, parts = [], [''] * 4
	for i in range(1, 4):
		parts[0] = s[:i]
		if not is_valid_part(parts[0]):
			continue
		for j in range(i + 1, i + 4):
			parts[1] = s[i:j]
			if not is_valid_part(parts[1]):
				continue
			for k in range(j + 1, j + 4):
				parts[2], parts[3] = s[j:k], s[k:]
				if (not is_valid_part(parts[2])
					or not is_valid_part(parts[3])):
					continue
				result.append('.'.join(parts) + '.')
	return result


print(compute_valid_ip_addresses('19216811'))