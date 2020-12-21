"""
Given two cycle-free singly linked lists, test if there is
a node that is common to both lists

If only a boolean is required to tell if the given lists
overlap, we can simply compare the tails of both lists, if
they are the same, then there must be an overlapping at some
node. The problem is that we need to return the node at which
the overlapping begins, if there is one

def overlapping_lists(l0, l1):
	def list_tail(l):
		while l.next:
			l = l.next
		return l

	return list_tail(l0) is list_tail(l1)
"""
class Node:
	def __init__(self, data=0, next_=None):
		self.data = data
		self.next = next_

	def __lt__(self, other):
		return self.data < other.data

	def __repr__(self):
		return f'Node: {self.data}'


def build_list(l):
	L = [Node(l[0])]
	for i in range(1, len(l)):
		L.append(Node(l[i]))
		L[i - 1].next = L[-1]
	return L


def overlapping_no_cycle_lists_naive(l0, l1):
	"""
	Loop through l0 and put all nodes in a hash map, then loop through
	l1 and check each node if they are also part of the l0

	O(n) time complexity
	O(n) space complexity
	n = len(l0) + len(l1)
	"""
	nodes_l0 = set()
	while l0:
		nodes_l0.add(l0)
		l0 = l0.next
	while l1:
		if l1 in nodes_l0:
			return l1 # overlapping found!
		l1 = l1.next
	return None # no overlapping


def overlapping_no_cycle_lists_naive2(l0, l1):
	"""
	Avoid extra space by using two nested loops

	O(1) space complexity
	O(n^2) time complexity
	n = len(l0) + len(l1)
	"""
	while l0:
		temp_l1 = l1
		while temp_l1:
			if temp_l1 is l0:
				return l0 # found overlapping node
			temp_l1 = temp_l1.next
		l0 = l0.next
	return None # not overlapping lists



def overlapping_no_cycle_lists(l0, l1):
	"""
	Advance the longer list until two lists are of
	the same length. Then advance two lists at the
	same time and check if the nodes are equal

	O(n) time complexity
	O(1) space complexity
	"""
	def list_len(l):
		length = 0
		while l:
			l = l.next
			length += 1
		return length

	l0_len, l1_len = list_len(l0), list_len(l1)

	if l0_len > l1_len:
		l0, l1 = l1, l0

	for _ in range(abs(l0_len - l1_len)):
		l1 = l1.next

	while l0 and l1 and l0 is not l1:
		l0, l1 = l0.next, l1.next
	return l0



l0 = build_list([1,2,3,4])
l1 = build_list([9,8,7])
l1[-1].next = l0[1]

print(overlapping_no_cycle_lists(l0[0], l1[0]))
