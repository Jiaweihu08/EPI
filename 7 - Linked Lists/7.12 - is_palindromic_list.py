"""
Given a singly linked list, test is the data stored in the list
for a palindrom
"""
class Node:
	def __init__(self, data=0, next_=None):
		self.data = data
		self.next = next_

	def __repr__(self):
		return f'Node: {self.data}'


def build_list(l):
	L = [Node(l[0])]
	for i in range(1, len(l)):
		L.append(Node(l[i]))
		L[i - 1].next = L[-1]
	return L


def is_palindromic_naive(L):
	"""
	O(n) space and time complexity
	"""
	s = []
	while L:
		s.append(L.data)
		L = L.next
	return all(s[i] == s[~i] for i in range(len(s) // 2))


def is_palindromic(L):
	"""
	Compare the first half of the list with the second half
	
	First iterate through the list and stop at the middle,
	this is achieved by using two pointers with the second
	pointer moving with the twice the speed of the first one.

	Then reverse the part of the list starting from the middle
	and compare the beginig of list with its reversed second
	half

	VISUALLY:
		original list L: 
					0 -> 1 -> 2 -> 3 -> 2 -> 1 -> 0
		L with its seconf half reversed:
					0 -> 1 -> 2 -> 3 <- 2 <- 1 <- 0
					|							  |
					L 						second half iter

	The same function used to reverse the second half of the
	list can be used again to restore the original list
	"""
	def reverse_list(s):
		iter_head = Node(0, s)
		it = iter_head.next
		while it.next:
			temp = it.next
			it.next, temp.next, iter_head.next = (temp.next,
												iter_head.next,
												temp)
		return iter_head.next

	slow = fast = L
	while fast and fast.next:
		fast, slow = fast.next.next, slow.next

	first_half_iter, second_half_iter = L, reverse_list(slow)

	while second_half_iter and first_half_iter:
		if second_half_iter.data != first_half_iter.data:
			return False
		second_half_iter, first_half_iter = (second_half_iter.next,
											first_half_iter.next)
	return True


L = build_list([0,1,2,3,1,0])[0]
is_palindromic(L)


