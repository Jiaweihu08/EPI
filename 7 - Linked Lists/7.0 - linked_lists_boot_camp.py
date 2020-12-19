"""
Some basic linked list manipulations
"""

class Node:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next


def search_list(node, key):
	while node and node.data != key:
		node = node.next
	return node


def insert_after(node, new_node):
	new_node.next = node.next
	node.next = new_node


def delete_after(node):
	node.next = node.next.next