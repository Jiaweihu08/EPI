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


def print_reversed_list_stack(L):
	"""
	Loop through the list and store the numbers in a stack
	Pop the stack until it's empty

	O(n) space and time complexity
	"""
	nodes = []
	while L:
		nodes.append(L.data)
		L = L.next

	while nodes:
		print(nodes.pop())


def print_reversed_list_reversing(L):
	"""
	Reverse the list, iterate through the reversed list and print
	the values, then reverse the reversed list

	O(n) time complexity
	O(1) space complexity
	"""
	def reverse_list(L):
		iter_head = Node(0, L)
		it = iter_head.next
		while it.next:
			temp = it.next
			it.next, temp.next, iter_head.next = (
				temp.next,
				iter_head.next,
				temp)
		return iter_head.next

	reversed_L = it = reverse_list(L)
	while it:
		print(it.data)
		it = it.next

	reverse_list(reversed_L)



L = build_list([0,1,2,3,4])[0]
print_reversed_list_reversing(L)


