import collections, functools


Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
	@functools.lru_cache(None)
	def optimum_subject_to_item_and_capacity(i, available_capacity):
		if i < 0:
			return 0

		without_this_item = (
			optimum_subject_to_item_and_capacity(i - 1, available_capacity))
		with_this_item = (
			items[i].value +
			optimum_subject_to_item_and_capacity(i - 1, available_capacity - items[i].weight)
			if available_capacity >= items[i].weight else 0)
		return max(without_this_item, with_this_item)

	return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


items = [Item(2, 3), Item(3, 6)]
capacity = 8
print(optimum_subject_to_capacity(items, capacity))