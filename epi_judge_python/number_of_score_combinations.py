from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.
    if final_score == 0:
        return 1

    rows = len(individual_play_scores)
    dp = [[0 for c in range(final_score + 1)] for r in range(rows + 1)]

    for r in range(1, rows + 1):
        for c in range(1, final_score + 1):d
            if c - individual_play_scores[r - 1] < 0:
                dp[r][c] = dp[r - 1][c] + 0
            elif c - individual_play_scores[r - 1] == 0:
                dp[r][c] = dp[r - 1][c] + 1
            else:
                dp[r][c] = dp[r - 1][c] + dp[r][c - individual_play_scores[r - 1]]
    
    return dp[rows][final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
