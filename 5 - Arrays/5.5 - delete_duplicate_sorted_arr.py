"""
Given a sorted array of integers, remove the duplicates
and return the number of unique entries
"""
import itertools


def delete_duplicates_naive(A):
	"""
	Time complexity: O(n)
	Space complexity: O(n)
	"""
	unique_A = []
	i = 0
	while i < len(A):
		unique_A.append(A[i])
		while i < len(A) - 1 and A[i] == A[i + 1]:
			i += 1
		i += 1

	return len(unique_A)


def delete_duplicates_naive_hash(A):
	unique_vals = set()
	unique_A = []
	for num in A:
		if num not in unique_vals:
			unique_vals.add(num)
			unique_A.append(num)
	return len(unique_A)


def delete_duplicates_move_left(A):
	"""
	Time complexity: O(n^2)
	"""
	if not A:
		return 0

	i = 1
	while i < len(A):
		if A[i - 1] == A[i]:
			A.pop(i)
		else:
			i += 1
	print(A)
	return i 


def delete_duplicates_groupby(A):
	return [k for k, g in itertools.groupby(A)]


def delete_duplicates(A):
	"""
	Move the unique element to the position where the last
	repeated element was found
	"""
	if not A:
		return 0

	to_write = 1
	for i in range(1, len(A)):
		if A[i] != A[i - 1]:
			A[to_write] = A[i]
			to_write += 1
	print(A)
	return to_write

A = [1,2,3,3,3,4,5,6,6,7,7,7,7,8]
# print(delete_duplicates_naive(A))
# print(delete_duplicates_naive_hash(A))
# print(delete_duplicates_move_left(A))
# print(delete_duplicates_groupby(A))
print(delete_duplicates(A))



