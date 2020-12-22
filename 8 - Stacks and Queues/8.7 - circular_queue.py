"""
Implement a queue API with an array and two pointers
head and tail poiting the begining and the end of the queue

The API should have a constructor that takes a size integer defining
the initial capacity of the queue, enquque and dequeue methods, and
a function that returns the number of elements stored in the queue

Implement dynamic resizing to support storing an arbitratily large
number of elements
"""
class Queue:
	SCALE_FACTOR = 2

	def __init__(self, capacity=1):
		self._data = [0] * capacity
		self._head = self._tail = 0
	
	def __repr__(self):
		return ','.join(map(str, self._data[self._head:self._tail]))

	def size(self):
		return self._tail - self._head

	def enqueue(self, data):
		if self._tail == len(self._data):
			self._data = self._data[self._head:] + self._data[:self._head]
			self._data += [0] * len(self._data) * (Queue.SCALE_FACTOR - 1)
			self._head, self._tail = 0, self.size()

		self._data[self._tail] = data
		self._tail += 1

	def dequeue(self):
		if self._head < self._tail:
			result = self._data[self._head]
			self._head += 1
			return result
		
		raise IndexError('Empty queue')



q = Queue(2)
for n in range(10):
	q.enqueue(n)
print(q)

for _ in range(5):
	print('removing:', q.dequeue())
print(q)


