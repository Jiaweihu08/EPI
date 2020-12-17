import math


def compute_primes_brute_force(n):
	def is_prime(n):
		"""
		For each number i in [2, n), there are (i - 2) operations
		Time complexity: O(n^2)
		"""
		for i in range(2, n):
			if n % i == 0:
				return False
		return True

	def is_prime_srqt(n):
		"""
		For each number i in [2, n), there are (sqrt(i) - 2) operations
		Time complexity: O(n^3/2)
		"""
		for i in range(2, math.floor(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
		return True

	return [x for x in range(2, n + 1) if is_prime_srqt(x)]


def compute_primes(n):
	primes = []
	is_prime = [False, False] + [True] * (n - 1)
	for p in range(2, n + 1):
		if is_prime[p]:
			primes.append(p)
			for i in range(p * 2, n + 1, p):
				is_prime[i] = False

	return primes


def generate_primes(n):
	"""
	Don't understand this solution
	"""
	if n < 2:
		return []
	size = (n - 3) // 2 + 1
	primes = [2]
	# is_prime => 3,5,7,9,11,13,15,17,19 ...
	is_prime = [True] * size
	for i in range(size):
		if is_prime[i]:
			p = i * 2 + 3
			primes.append(p)
			for j in range(2 * i**2 + 6 * i + 3, size, p):
				is_prime[j] = False
	return primes


# print(compute_primes_brute_force(19))
print(generate_primes(19))
