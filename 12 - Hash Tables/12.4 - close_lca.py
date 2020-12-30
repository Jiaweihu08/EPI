"""
Design an algorithm for find the lca of two given nodes that only
depends on their distance to the lca
"""
def lca(node1, node2):
	nodes_on_search_path = set()
	while node1 or node2:
		if node1:
			if node1 in nodes_on_search_path:
				return node1
			nodes_on_search_path.add(node1)
			node1 = node1.parent

		if node2:
			if node2 in nodes_on_search_path:
				return node2
			nodes_on_search_path.add(node2)
			node2 = node2.parent
	raise ValueError('Nodes 1 and 2 are not from the same tree')