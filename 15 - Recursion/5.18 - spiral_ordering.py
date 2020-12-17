def matrix_in_spiral_order(A):
	"""
	The key insight for this problem is to notice that generating a
	spiral ordering of a matrix is the same as reading the each layer
	of the matrix clockwise

	In this solution, for each layer we do four horizontal or vertical
	readings, each time starting at the first available position and
	always leaving an offset of elements in the same row/column
	"""
	def matrix_layer_in_clockwise(offset):
		if offset == len(A) - 1 - offset:
			spiral_ordering.append(A[offset][offset])
			return

		spiral_ordering.extend(A[offset][offset:-1 - offset])
		spiral_ordering.extend(
			list(zip(*A))[-1 - offset][offset:-1 - offset])
		spiral_ordering.extend(A[-1 - offset][-1 - offset:offset:-1])
		spiral_ordering.extend(
			list(zip(*A))[offset][-1 - offset:offset:-1])

	spiral_ordering = []
	for offset in range((len(A) + 1) // 2):
		matrix_layer_in_clockwise(offset)
	return spiral_ordering


def matrix_in_spiral_ordering_2(A):
	"""
	In the previous solution we extend the ordering four times for each
	layer and they are almost identical

	The same reading could be done also by repeatedly reading elements
	in a given direction and then make an appropiated turn when a limit
	is reached
	"""
	not_present = 0
	for row in A:
		for num in row:
			not_present = min(num, not_present)
	not_present -= 1

	shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
	direction = i = j = 0
	spiral_ordering = []

	for _ in range(len(A) ** 2):
		spiral_ordering.append(A[i][j])
		A[i][j] = not_present
		next_i, next_j = i + shift[direction][0], j + shift[direction][1]
		if (next_i not in range(len(A))
				or next_j not in range(len(A))
				or A[next_i][next_j] == not_present):
			# 0/1/2/3 & 3 = 0/1/2/3, 4 & 3 = 0
			# same as applying mod 4: direction = (direction + 1) % 4
			direction = (direction + 1) & 3
			next_i, next_j = i + shift[direction][0], j + shift[direction][1]
		i, j = next_i, next_j

	return spiral_ordering


def get_matrix(n):
	matrix = []
	row = []
	for num in range(1, n ** 2 + 1):
		row.append(num)
		if len(row) == n:
			print(row)
			matrix.append(row)
			row = []
	return matrix


A = get_matrix(5)
print()
print(matrix_in_spiral_ordering_2(A))


