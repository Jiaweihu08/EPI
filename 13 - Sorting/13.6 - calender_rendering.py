"""
Given an array of events defined by a starting and an ending time,
find the max number of events that are happening at the same time

For each event in the array, go through all other events and check
if there is an overlap between them, if true, increment the counter
for the current event and redefine the event's start point as the
largest start point of the two and the end point as the smallest one
of the two.

The time complexity is O(n^2)

Set a counter to count for endpoints visited, if the endpoint is the
start of an event, increment the count by 1, otherwise decrease it by
one. For this method to work, we need to sort the enpoints, and starts
should come before ends.

The intuition behind it is that, when starting or finishing an event,
we count how many event are still happening.
"""
import collections


Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_num_concurrent_event_n2(A):
	result = 0
	for e in A:
		curr_count = 0
		for comp_e in A:
			if e.start <= comp_e.finish and e.finish >= comp_e.start:
				e = Event(max(e.start, comp_e.start),
							min(e.finish, comp_e.finish))
				curr_count += 1
		result = max(curr_count, result)
	return result



def find_max_num_concurrent_event(A):
	Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
	E = [
		p for e in A
		for p in (Endpoint(e.start, True), Endpoint(e.finish, False))
		]
	E.sort(key=lambda e: (e.time, not e.is_start))

	max_num_concurrent_event = num_concurrent_event = 0
	for e in E:
		if e.is_start:
			num_concurrent_event += 1
			max_num_concurrent_event = max(max_num_concurrent_event,
										num_concurrent_event)
		else:
			num_concurrent_event -= 1

	return max_num_concurrent_event



a = [[1,5],[6,10],[11,13],[14,15],[2,7],[8,9],[12,15],[4,5],[9,17],[9,10]]
A = [Event(s, e) for s, e in a]
print(find_max_num_concurrent_event(A))

