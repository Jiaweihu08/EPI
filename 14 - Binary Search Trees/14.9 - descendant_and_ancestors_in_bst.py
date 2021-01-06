"""
Given two nodes in a bst and a middle node, check if one node is
the proper ancestor and the other is the proper descendant of the
middle node.
"""
def pair_includes_ancestor_and_descendant_of_m(
	possible_anc_or_desc_0, possible_anc_or_desc_1, middle):
	"""
	Start searching from middle going downwards, if any of the two nodes are found
	as a child of the middle node, defined it as the proper descendant, and the
	other one as a candidate for proper ancestor.

	We then start searching for middle from the candidate ancestor,
	and return true if the middle is found from this candidate.

	O(h) worst-case time complexity, h is the tree height
	"""
	def search_target(source, target):
		if not source:
			return None
		if source in target:
			return source
		return (search_target(source.left, target) or
				search_target(source.right, target))

	middle_target = [possible_anc_or_desc_0, possible_anc_or_desc_1]
	descendant = (search_target(middle.left, middle_target) or
				search_target(middle.right, middle_target))
	
	if not descendant:
		return False

	ancestor = (possible_anc_or_desc_0 if possible_anc_or_desc_1 is descendant
					else possible_anc_or_desc_1)

	return search_target((ancestor.left if ancestor.data > middle.data
		else ancestor.right), [middle]) is middle


def pair_includes_ancestor_and_descendant_of_m_epi(
	possible_anc_or_desc_0, possible_anc_or_desc_1, middle):
	"""
	This is a slightly more efficient algorithm in comparison with the previous one.

	We start searching from the candidate nodes for middle, if its not found, return
	False. The search that found the middle node is defined as the proper ancestor
	then we start from middle and search for the other node.

	The previous implementation of search was purely DFS, and this one is guided by
	the target value.
	"""
	search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1

	while (search_0 is not middle and search_0 is not possible_anc_or_desc_1
		and search_1 is not middle and search_1 is not possible_anc_or_desc_0
		and (search_0 or search_1)):
		if search_0:
			search_0 = (search_0.left if search_0.data > middle.data
				else search_0.right)

		if search_1:
			search_1 = (search_1.left if search_1.data > middle.data)
				else search_1.right

	if ((search_0 is not middle and search_1 is not middle)
			or search_0 is possible_anc_or_desc_1
			or search_1 is possible_anc_or_desc_0):
		return False

	def search_target(source, target):
		while source and source is not target:
			source = source.left if source.data > target.data else source.right
		return source is target

	return search_target(middle, possible_anc_or_desc_1
		if search_0 is middle else possible_anc_or_desc_0)


