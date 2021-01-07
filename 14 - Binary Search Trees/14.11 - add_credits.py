"""
Augmented BST

Say that we want to find the number of nodes in a BST that have their keys
within a given interval. One way to do it is to perform a range lookup using
DFS traversal and avoid searching subtrees that we don't need to.


def range_count_in_bst(tree, interval):
	def range_count_in_bst_helper(tree):
		if not tree:
			return
		if interval.left <= tree.data <= interval.right:
			range_count_in_bst_helper(tree.left)
			count[0] += 1
			range_count_in_bst_helper(tree.right)
		elif interval.left > tree.data:
			range_count_in_bst_helper(tree.right)
		else:
			range_count_in_bst_helper(tree.left)
	count = [0]
	range_count_in_bst_helper(tree)
	return count[0]


Another approach is to first find the first element in BST that is >= than
the left limit of the interval and recursively compute the successor of the
nodes.


def range_count_in_bst(tree, interval):
	def find_successor(node):
		if node.right:
			node = node.right
			while node.left:
				node = node.left
			return node

		while node.parent and node.parent.right is node:
			node = node.parent
		return node.parent

	def find_lower_bound(tree):
		subtree, lower_bound_so_far = tree, None
		while subtree:
			if subtree.data >= interval.left:
				lower_bound_so_far, subtree = subtree, subtree.left
			else:
				subtree = subtree.right
		return lower_bound_so_far

	count = 0
	first_node_in_interval = find_lower_bound(tree)
	while first_node_in_interval:
		count += 1
		first_node_in_interval = find_successor(first_node_in_interval)
	return count


Both approaches have the worst-case time complexity of O(h + m), where h is
the depth of the tree and m the number of keys from the tree that lie in the
interval. When m is large, these approaches will be slow.

Improved efficiency can be achieved by using augmented BST - adding a size
field that stores the number of nodes in the subtree rooted at that node.In
this way, the number of nodes that have keys smaller than the one of the
current node is simply its left subtree' size.

Say that we want to solve the problem of finding the number of nodes in a BST
that have keys smaller that a given value k. Search for the largest node in
BST whose key is smaller than k using the find_lower_bound function, with
some modifications. If the current node's key is greater than k, we go left
and do nothing. If it the key is smaller than k, we move on to its right
child and increment the counter by its left subtree' size plus one. The
programm would terminate when a null is reached, or a node with key k is
accountered, in which case the counter is incremented by the size of its left
subtree.


To find the number of nodes with keys that lie in a given interval, compute
the number of nodes with keys smaller than the interval's lower bound and
the number of nodes with keys greater than the interval's upper bound with
the above-mentions method and subtract the both from the total number of
nodes, which is the size field of the root node.

The time complexity of this approach is O(h), with h being the height of the
BST. which is much better than O(h + m), when m is large.


14.11

Design a data structure that implements the following methods:
1 - lookup: return credits associated with the specified client
2 - add_to_all: add a given value c to credit counts of all clients
3 - remove: remove clients with a given number of credit
4 - insert: add a client with a specified credit, remove any existing entry
of that client
5 - max: return the client with max number of credits

"""
import bintrees


class ClientsCreditsInfo:
	def __init__(self):
		self._offset = 0
		self._client_to_credit = {}
		self._credit_to_clients = bintree.RBTree()

	def insert(self, client_id, c):
		self.remove(client_id)
		self._client_to_credit[client_id] = c - self._offset
		self._credit_to_clients.setdefault(c - self._offset,
			set()).add(client_id)

	def remove(self, client_id):
		credit = self._client_to_credit.get(client_id)
		if credit is not None:
			self._credit_to_clients.remove(client_id)
			if not self._credit_to_clients[client_id]:
				del self._credit_to_clients[client_id]
			del self._client_to_credit[client_id]
			return True
		return False

	def lookup(self, client_id):
		credit = self._client_to_credit[client_id]
		return -1 if not credit else credit + self._offset

	def all_to_all(self, c):
		self._offset += c

	def max(self):
		if not self._credit_to_clients:
			return ''
		clients = self._credit_to_clients.max_items()[1]
		return '' if not clients else next(iter(clients))

