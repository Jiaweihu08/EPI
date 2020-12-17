# def plus_one(A):
# 	if A[-1] != 9:
# 		A[-1] += 1
# 		return A

# 	i = len(A) - 1
# 	while i >= 0 and A[i] == 9:
# 		A[i] = 0
# 		i -= 1

# 	if i >= 0:
# 		A[i] += 1

# 	else:
# 		A = [1] + A

# 	return A


def plus_one(A):
	A[-1] += 1
	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i - 1] += 1
	else:
		if A[0] == 10:
			A[0] = 1
			A.append(0)

	return A

A = [1,2,9]
A = plus_one(A)
print(A)

