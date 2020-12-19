"""
Given a linked list L and two integers s and f, return the
linked list L with nodes from s to f(inclusive) reversed

The numbering begins at 1.

e.g.
	L: H - 1 - 3 - 5 - 7 - 9, s:2, f: 4
	L: H - 1 - 7 - 5 - 3 - 9
"""
class Node:
	def __init__(self, data=0, next_=None):
		self.data = data
		self.next = next_


def build_list(l):
	head = tail = Node(l[0])
	for i in range(1, len(l)):
		tail.next = Node(l[i])
		tail = tail.next
	return head


def show_list(L):
	while L:
		print(L.data, end=' ')
		L = L.next
	print()


def reverse_sublist(L, s, f):
	dummy_head = sublist_head = Node(0, L)
	for _ in range(1, s):
		sublist_head = sublist_head.next

	sublist_iter = sublist_head.next
	for _ in range(f - s):
		temp = sublist_iter.next
		sublist_iter.next, temp.next, sublist_head.next = (
			temp.next,
			sublist_head.next,
			temp)


def move_element_to_tail(L, idx):
	"""
	Given a linked list and an index, move the element specified
	by the index to the end of the list
	"""
	head = temp_head = Node(0, L)
	for _ in range(1, idx):
		temp_head = temp_head.next

	node = temp_head.next
	while node.next:
		temp = node.next
		node.next, temp.next, temp_head.next, temp_head = (
			temp.next, node, temp, temp)
	return head.next



L1 = build_list([2,5,7,8,9])

reverse_sublist(L1, 2, 4)
# L1 = move_element_to_tail(L1, 2)

show_list(L1)
