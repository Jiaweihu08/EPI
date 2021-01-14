"""
Given a score s and an array representing scores for each individual
plays, count the number of combinations of the individual play scores
that sum up to s

Say that the final score s is 12 and the individual play scores are 2,
3, and 7. Assume that we only have plays that award 2 points, the results
for scores s from 0 to 12 are represented by an array full of ones except
positions where the index i can be evenly divided by 2:
				A[2] = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
					 	0  1  2  3  4  5  6  7  8  9  10 11 12

Now let's compute for the case where we have plays that award 2 and 3
points and let's do that using the results from the previous case.

When we only have 2 point plays, there was only one way to add up to 12:
2 + 2 + 2 + 2 + 2 + 2 = 12, if we there to introduce one 3, then the rest
of 2s must sum up to 12 - 3 = 9, for that, all we need to do is to check
how many combinations we have that sum to 9 using 2s, i.e. A[2][9]. The
same for using two 3s, 2s must sum to 12 - 2 x 3 = 6. The process is repeated
until we have a sum of 3s that exceeds 12, in this case, 4 x 3 = 12.

				A[3][12] = A[2][0] + A[2][3] + A[2][6] + A[2][9] + A[2][12]
				A[3][9] = A[2][0] + A[2][3] + A[2][6] + A[2][9]
				A[3][6] = A[2][0] + A[2][3] + A[2][6]
				...

A closer look can reveal the following:
				A[3][i] = A[2][i] + A[3][i - 3]
"""
def num_combinations_for_final_score_n2s(final_score, individual_play_scores):
	num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]
	for i in range(len(individual_play_scores)):
		for j in range(1, final_score + 1):
			without_this_play = (num_combinations_for_score[i - 1][j] if i >= 1 else 0)
			with_this_play = (
				num_combinations_for_score[i][j - individual_play_scores[i]]
				if j >= individual_play_scores[i] else 0)
			num_combinations_for_score[i][j] = (without_this_play + with_this_play)
	return num_combinations_for_score[-1][-1]


def num_combinations_for_final_score_n1s(final_score, individual_play_scores):
	num_combinations_for_score = [1] + [0] * final_score
	for individual_score in individual_play_scores:
		for i in range(individual_score, final_score + 1):
			num_combinations_for_score[i] += num_combinations_for_score[i - individual_score]
	return num_combinations_for_score[-1]


final_score = 12
individual_play_scores = [2, 3, 7]
print(num_combinations_for_final_score_n1s(final_score, individual_play_scores))
