"""
Compute steps to move n discs from one peg to another following
the rules of Tower of Hanoi.

Say that we have three pegs and initially all n discs are stacked
on the first one. The goal is to move all n discs from peg 1 to
peg 2, using all three pegs. No disc is allowed to be placed on
another one that is larger than itself.

The solution to the problem is to first move n - 1 discs from peg
1 to peg 3, move the nth disct to peg 2, and finish by moving the
n - 1 discs from peg 3 to peg 2.
"""
def compute_hanoi_tower(num_rings):
	def compute_hanoi_step(num_rings, from_peg, to_peg, use_peg):
		if num_rings > 0:
			compute_hanoi_step(num_rings - 1, from_peg, use_peg, to_peg)
			pegs[to_peg].append(pegs[from_peg].pop())
			result.append([from_peg, to_peg])
			compute_hanoi_step(num_rings - 1, use_peg, to_peg, from_peg)
	
	NUM_PEGS = 3
	result = []
	pegs = [list(reversed(range(1, num_rings+1)))]
			+ [[] for _ in range(1, NUM_PEGS)]
	compute_hanoi_step(num_rings, 0, 1, 2)
	
	return result


compute_hanoi_tower(5)