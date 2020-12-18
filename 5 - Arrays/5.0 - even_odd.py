"""
Given an array of integers, reorder the array so the
even entries appear first in the array

It is easy to find a O(n) space complexity solution by
placing odd and even entries in two different arrays and
merge them at the end

To avoid O(n) space complaxity we can split the array in
three domains: 

even: A[:next_even],
unclassified: A[next_even:next_odd],
and odd: A[next_odd:]

and place the elements from the unclassified domain to
either even or odd according to their values
"""
def even_odd(A):
	next_even, next_odd = 0, len(A) - 1
	while next_even < next_odd:
		if A[next_even] % 2 == 0:
			next_even += 1
		else:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd -= 1


A = [1,3,2,4,7,9,6]
even_odd(A)
print(A)