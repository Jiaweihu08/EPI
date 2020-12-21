"""
Given a linked list L and a integer k, remove L's kth last element without
recording the length of the list
"""
class Node:
	def __init__(self, data=0, next_=None):
		self.data = data
		self.next = next_


def remove_kth_last(L, k):
	dummy_head = Node(0, L)
	first = dummy_head.next
	for _ in range(k):
		first = first.next

	second = dummy_head
	while first:
		first, second = first.next, second.next
	second.next = second.next.next
	return dummy_head.next