"""
Given a file with around a billion IP addresses, find the one that
is missing from all possible 32 bits addresses

All possible 32 bits IP addresses range from
00000000.00000000.00000000.00000000 to 11111111.11111111.11111111.11111111
with a total of 2 ** 32 values

The naive approach is to sort addresses in the file and compute the gap every
two consecutive values, if the gap is greater than 1, the missing value is found

This approach takes O(nlog(n)) time to sort and the space complexity is large

An alternative is to iterate through the file and count the values that start with
0 and 1, if all possible values are in the file, then the count for these values
should both be 2 ** 31. The missing IP address is the one that has the count equal
to 2 ** 31 - 1. Say that the missing IP address starts with 0, now we can iterate the
file again counting values that start with 01 and 00, the process is repeated 32 times
to find the missing value.

If we have more RAM available, we can start counting the first 16 bits instead of only
the leading bit. We use an array of size 2 ** 16 to count the values that beging with
0, 1, 2, ..., 2 ** 16 - 1. The count that has a value less than 2 ** 16 is the one of
the missing IP address. The use the same procedure again now counting values that start
with the one found in the last step to find the missing IP
"""
import itertools


def find_missing_ip(stream):
	num_bucket = 1 << 16 # 2 ** 16
	counter = [0] * num_bucket
	# creating two copies of stream
	stream, stream_copy = itertools.tee(stream) 
	for x in stream:
		# iterate over stream and count the number of values
		# with every possible leading 16 bits
		upper_part =  x >> 16
		counter[upper_part] += 1

	bucket_capacity = 1 << 16
	# find the bucket with a count less than 2 ** 16
	candidate_bucket = next(i for i, c in enumerate(counter)
		if c < bucket_capacity)

	candidates = [0] * bucket_capacity
	for x in stream_copy:
		upper_part_x = x >> 16
		if upper_part_x == candidate_bucket:
			# if the first part of x matches with candidate_bucket,
			# extract its second part
			lower_part_x = ((1 << 16) - 1) & x
			candidates[lower_part_x] = 1

	for i, v in enumerate(candidates):
		if v == 0:
			return (candidate_bucket << 16) | i



