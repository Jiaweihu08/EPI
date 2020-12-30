"""
Create a cache for looking up prices of books identified by their ISBN.
Implement lookup, insert, and erase methods. Use the LRU policy for cache
eviction - If the number of books exceeds the capacity of the cache when
inserting a new book, replace the oldest operated book with the new one

Use a hash table to store ISBN identifiers of the books and their prices,
ISBN are used as keys. We also keep a counter to keep track of the number
of insertions and lookups done to each book, when the size of the hash
table exceeds the capacity, the book with the least count is removed to
free space

This requires O(n) time to find the ISBN with the least count, remove it,
and place the new book in the hash table, so insertion will take O(n) time

To improve the efficienty we can avoid processing all entries in the hash
table when looking for the oldest ISBN. Use a queue to store the insertion
order of the items. Move the elements to the end of the queue each time
we do an insert or lookup. When the capacity is reached, remove the element
at the front of the queue and insert the new one

An OrderedDict is ideal in this scenario since it keeps track of the order
of insertion of the items in the dictionary. When performing insertions or
lookups, we first remove the element from the dictionary and then add it back,
the looked or inserted element will now be the most recently used on, the LRU
element is always at the begining of the queue
"""
import collections


class LruCache:
	def __init__(self, capacity):
		self._isbn_price_table = collections.OrderedDict()
		self._capacity = capacity

	def lookup(self, isbn):
		if isbn not in self._isbn_price_table:
			return -1
		price = self._isbn_price_price.pop(isbn)
		self._isbn_price_table[isbn] = price
		return price

	def insert(self, isbn, price):
		if isbn in self._isbn_price_table:
			price = self._isbn_price_price.pop(isbn)
		elif len(self._isbn_price_table) == self.capacity:
			self._isbn_price_price.popitem(last=False)
		self._isbn_price_table[isbn] = price

	def erase(self, isbn):
		return (self._isbn_price_table.pop(isbn, None) is not None)


# class LRU(collections.OrderedDict):
#     def __init__(self, maxsize=128, /, *args, **kwds):
#         self.maxsize = maxsize
#         super().__init__(*args, **kwds)

#     def __getitem__(self, key):
#         value = super().__getitem__(key)
#         self.move_to_end(key)
#         return value

#     def __setitem__(self, key, value):
#         if key in self:
#             self.move_to_end(key)
#         super().__setitem__(key, value)
#         if len(self) > self.maxsize:
#             oldest = next(iter(self))
#             del self[oldest]

