from collections import namedtuple

Rect = namedtuple('Rect', ('x','y','width','height'))

def get_rect_intersect(r1, r2):
	"""
	assuming x grows going right
	y grows going down
	"""
	def is_intersect(r1, r2):
		return (r1.x <= r2.x + r2.width and r2.x <= r1.x + r1.width
			and r1.y <= r2.y + r2.height and r2.y <= r1.y + r1.height)

	if not is_intersect(r1, r2):
		return Rect(0, 0, -1, -1)

	return Rect(max(r1.x, r2.x), min(r1.y, r2.y),
		min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
		min(r1.y + r1.height, r2.y + r2.height) - min(r1.y, r2.y))

