"""
Given an array of intervals, compute the unions expressed as 
a set of disjoint intervals
"""
import collections


Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
	if not intervals:
		return []

	intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
	result = [intervals[0]]
	for i in intervals:
		if intervals and (i.left.val < result[-1].right.val or
							(i.left.val == result[-1].right.val and
								(i.left.is_closed or result[-1].right.is_closed))):
			if (i.right.val > result[-1].right.val or
				(i.right.val == result[-1].right.val and i.right.is_closed)):
				result[-1] = Interval(result[-1].left, i.right)
		else:
			result.append(i)
	return result


a = [((False, 0),(False, 3)), ((True, 5), (False, 7)), ((False, 9), (True, 11)),
	((True, 12), (True, 14)), ((True, 1), (True, 1)), ((True, 3), (False, 4)),
	((True, 7), (False, 8)), ((False, 12), (True, 16)), ((True, 2), (True, 4)),
	((True, 8), (False, 11)), ((False, 13), (False, 15)), ((False, 16), (False, 17))]

A = [(Endpoint(*s), Endpoint(*e)) for s, e in a]

intervals = [Interval(*i) for i in A]
intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))

print(union_of_intervals(intervals))
