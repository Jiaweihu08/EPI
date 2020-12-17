def compute_hanoi_tower(num_rings):
	def compute_hanoi_step(num_rings, from_peg, to_peg, use_peg):
		if num_rings > 0:
			compute_hanoi_step(num_rings - 1, from_peg, use_peg, to_peg)
			pegs[to_peg].append(pegs[from_peg].pop())
			print(pegs)
			result.append([from_peg, to_peg])
			compute_hanoi_step(num_rings - 1, use_peg, to_peg, from_peg)
	
	NUM_PEGS = 3
	result = []
	pegs = [list(reversed(range(1, num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]
	compute_hanoi_step(num_rings, 0, 1, 2)
	
	return result

if __name__ == '__main__':
	compute_hanoi_tower(5)