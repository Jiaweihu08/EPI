"""
Given an array of integers and a index integer i, reorder
the array so the elements smaller that A[i] are on A[i]'s
left side, those larger than A[i] are placed on it's right
side

Again, O(n) space solution is trivial, build three arrays
less_than, equal_to, and larger_than and place each entrie
in one of the three arrays accoding to their values and return
the merged array at the end

The O(1) space solution can be achieved by performing swappings
either looping through the array twice moving smaller entries
to the fron and larger entries to the end or, as in the case of
exercise 5.0, define three regions in the array and swap the
entries from the unclassified region to their corresponding regions
"""


# import random
# def quick_sort(A, l, r):
# 	if l >= r:
# 		return

# 	def partition_3(A, l, r):
# 		pivot = A[l]
# 		j = l
# 		count = 1
# 		for i in range(l+1, r):
# 			if A[i] < pivot:
# 				j += 1
# 				A[i], A[j] = A[j], A[i]
# 			elif A[i] == pivot:
# 				count += 1

# 		A[l], A[j] = A[j], A[l]
# 		return j, j + count

# 	k = random.randint(l, r - 1)
# 	A[l], A[k] = A[k], A[l]

# 	m1, m2 = partition_3(A, l, r)

# 	quick_sort(A[l, m1])
# 	quick_sort(A[m1, r])


def dutch_flag_partition_brute_force(A, pivot_index):
	"""
	O(n) time complexity
	O(n) space complexity
	"""
	pivot = A[pivot_index]
	less_than, equal_to, larger_than = [], [], []
	for num in A:
		if num < pivot:
			less_than.append(num)
		elif num == pivot:
			equal_to.append(num)
		else:
			larger_than.append(num)
	return less_than + equal_to + larger_than


def dutch_flag_partition_n2(A, pivot_index):
	"""
	O(n^2) time complexity
	O(1) space complexity
	"""
	pivot = A[pivot_index]
	for i in range(len(A)):
		for j in range(i + 1, len(A)):
			if A[j] < pivot:
				A[i], A[j] = A[j], A[i]
				break

	for i in reversed(range(len(A))):
		for j in reversed(range(i)):
			if A[j] > pivot:
				A[i], A[j] = A[j], A[i]
				break


def dutch_flag_partition_n(A, pivot_index):
	"""
	O(n) time complexity
	O(1) space complexity
	"""
	pivot = A[pivot_index]
	smaller, larger = 0, len(A) - 1
	for i in range(len(A)):
		if A[i] < pivot:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1

	for i in reversed(range(len(A))):
		if A[i] > pivot:
			A[i], A[larger] = A[larger], A[i]
			larger -= 1


def dutch_flag_partition(A, pivot_index):
	pivot = A[pivot_index]
	"""
	bottom group: A[:smaller]
	middle group: A[smaller:equal]
	unclassified group: A[equal:larger]
	top group: A[larger:]
	"""
	smaller, equal, larger = 0, 0, len(A)
	while equal < larger:
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller + 1, equal + 1
		
		elif A[equal] == pivot:
			equal += 1

		else:
			larger -= 1
			A[equal], A[larger] = A[larger], A[equal]
			

A = [1,4,0,5,3,4]
pivot_index = 4
print(pivot_index, A[pivot_index])
dutch_flag_partition(A, pivot_index)
print(A)

