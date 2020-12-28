import itertools
import heapq

def top_k(k, stream):
	min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
	heapq.heapify(min_heap)
	for next_string in stream:
		# add the next string and remove the smallest one
		heapq.heappushpop(min_heap, (len(next_string), next_string))
	return [p[1] for p in heapq.nsmallest(k, min_heap)]


stream = iter(['nihao', 'wobuhao', 'wohenhao', 'nihaoma', 'yibanbanba'])
print(top_k(3, stream))