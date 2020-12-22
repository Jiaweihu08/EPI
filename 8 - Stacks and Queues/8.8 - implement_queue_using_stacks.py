"""
Implement queue using stacks
"""
class Queue:
	def __init__(self):
		self._enq = []
		self._deq = []

	def enqueue(self, x):
		self._enq.append(x)

	def dequeue(self):
		if not self._deq:
			while self._enq:
				self._deq.append(self._enq.pop())
		return self._deq.pop()


q = Queue()
for i in range(10):
	q.enqueue(i)
	if i % 4 == 0:
		print(q.dequeue())
print(q)


