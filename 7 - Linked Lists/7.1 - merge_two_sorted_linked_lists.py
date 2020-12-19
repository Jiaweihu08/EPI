"""
Merge two sorted linked lists so the result is also sorted
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

		
def merge_sorted(L1, L2):
	dummy_head = tail = Node()
	
	while L1 and L2:
		if L1.data <= L2.data:
			tail.next, L1 = L1, L1.next
		else:
			tail.next, L2 = L2, L2.next
		tail = tail.next

	tail.next = L1 or L2
	return dummy_head.next




l1 = [2,5,7]
l2 = [1,3,6]

L1 = build_list(l1)
L2 = build_list(l2)

L = merge_sorted(L1, L2)
show_list(L)

