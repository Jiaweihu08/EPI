import collections
import heapq


# vanilla counting sort
def vanilla_counting_sort(A):
	"""
	Works in O(n) time if all vals are positive and
	the max val isn't too large
	"""
	num_to_count = [0] * (max(A) + 1) # O(n)
	for num in A: # O(n)
		num_to_count[num] += 1

	for i in range(1, len(num_to_count)): #O(m), m=max(A)
		num_to_count[i] += num_to_count[i - 1]
	
	result = [0] * len(A) # O(n) space
	for num in A: # O(n)
		idx = num_to_count[num - 1] if num != 0 else 0
		result[idx] = num
		num_to_count[num - 1] += 1
	return result


# in-place counting sort
def grouping(A):
	# O(n) time, O(m) space
	val_to_count = collections.Counter(A)
	# O(m) space
	val_to_offset, offset = {}, 0

	# O(mlog(m)) time, O(m) space
	min_heap = list(val_to_count.keys())
	heapq.heapify(min_heap)

	while min_heap: # O(mlog(m))
		val = heapq.heappop(min_heap)
		val_to_offset[val] = offset
		offset += val_to_count[val]

	# for val, count in val_to_count.items():
	# 	val_to_offset[val] = offset
	# 	offset += count

	# O(n) time
	while val_to_count:
		from_val = next(iter(val_to_count))
		from_idx = val_to_offset[from_val]
		to_val = A[from_idx]
		to_idx = val_to_offset[to_val]

		A[from_idx], A[to_idx] = A[to_idx], A[from_idx]
		val_to_count[to_val] -= 1
		if val_to_count[to_val]:
			val_to_offset[to_val] = to_idx + 1
		else:
			del val_to_count[to_val]

	print(A)





A = [3,2,3,7,5,5,6,5]
print(A)
print(list(range(len(A))))
grouping(A)