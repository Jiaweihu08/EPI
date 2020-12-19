"""
Given a linked list, test if the list contains a cycle.
If true, return the node at which the cycle begins and
null otherwise
"""
class Node:
	def __init__(self, data=0, next_=None):
		self.data = data
		self.next = next_

	def __repr__(self):
		return f'Node: {self.data}'


def build_list(l):
	head = Node(l[0])
	L = [head]
	for i in range(1, len(l)):
		head.next = Node(l[i])
		head = head.next
		L.append(head)
	return L


def has_cycle_brute_force1(L):
	"""
	O(n) time complexity
	O(n) space complexity
	"""
	unique_nodes = set()
	while L:
		if L.data in unique_nodes:
			return L
		unique_nodes.add(L.data)
		L = L.next
	return None


def has_cycle_brute_force2(L):
	"""
	O(n^n) time complexity
	O(1) space complexity
	"""

	outer_loop = L
	outer_count = 1
	while outer_loop:
		inner_loop, outer_loop = L, outer_loop.next
		inner_count, outer_count = 1, outer_count + 1
		while inner_loop is not outer_loop:
			inner_loop = inner_loop.next
			inner_count += 1
		if inner_count != outer_count:
			return outer_loop
	return None


def has_cycle(head):
	def cycle_len(end):
		start, steps = end, 0
		while True:
			start = start.next
			steps += 1
			if start is end:
				return steps

	fast = slow = head

	while fast and fast.next:
		slow, fast = slow.next, fast.next.next
		if slow is fast:
			cycle_len_advanced_iter = head
			for _ in range(cycle_len(slow)):
				cycle_len_advanced_iter = cycle_len_advanced_iter.next

			it = head
			while it is not cycle_len_advanced_iter:
				it = it.next
				cycle_len_advanced_iter = cycle_len_advanced_iter.next
			return it
	return None



l = [0,1,2,3,5,0,9,8,11]
nodes = build_list(l) # linear linked list
nodes[-1].next = nodes[2] # connect the last node to the third node

print(nodes)
print(has_cycle(nodes[0]))

