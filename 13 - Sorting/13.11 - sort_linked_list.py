"""
Sort a given singly linked list in-place
"""
def sort_list_n2(L):
	dummy_head = ListNode(0, L)
	while L and L.next:
		if L.data > L.next.data:
			target, pre = L.next, dummy_head
			while pre.next.data < target.data:
				pre = pre.next
			temp, pre.next, L.next = pre.next, target, target.next
			target.next = temp
		else:
			L = L.next
	return dummy_head.next


def stable_sort_list(L):
	def merge_two_sorted_lists(L1, L2):
		dummy_head = tail = ListNode()

		while L1 and L2:
			if L1.data <= L2.data:
				tail.next, L1 = L1, L1.next
			else:
				tail.next, L2 = L2, L2.next
			tail = tail.next

		tail.next = L1 or L2
		return dummy_head.next


	if L is None or L.next is None:
		return L

	pre_slow, slow, fast = None, L, L
	while fast and fast.next:
		pre_slow = slow
		slow, fast = slow.next, fast.next.next

	if pre_slow:
		pre_slow.next = None
	return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


	