"""
Given a linked list with 0-based counting, return the list with
the nodes with even indices appearing first followed by the nodes
with odd indices
"""
class Node:
	def __init__(self, data=0, next_=None):
		self.data = data
		self.next = next_

def build_list(l):
	L = [Node(l[0])]
	for i in range(1, len(l)):
		L.append(Node(l[i]))
		L[i - 1].next = L[-1]
	return L

def even_odd_merge1(L):
	if L is None:
		return L

	dummy_head = Node(-1, L)
	odd_head = odd = Node()
	even = dummy_head.next
	while even.next:
		odd.next = even.next
		odd = odd.next
		if odd.next:
			even.next = odd.next
			even = even.next
		else:
			break
	odd.next = None
	even.next = odd_head.next
	return dummy_head.next


def even_odd_merge(L):
	if L is None:
		return L

	even_dummy_head, odd_dummy_head = Node(), Node()
	tails, turn = [even_dummy_head, odd_dummy_head], 0
	while L:
		tails[turn].next = L
		tails[turn] = tails[turn].next
		L = L.next
		turn ^= 1
	tails[0].next = odd_dummy_head.next
	tails[1].next = None
	return even_dummy_head.next


L = build_list([0,1,2,3,4,5])
L = even_odd_merge1(L[0])
while L:
	print(L.data)
	L = L.next

