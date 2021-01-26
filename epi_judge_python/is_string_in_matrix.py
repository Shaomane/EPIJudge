from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    N = len(grid)
    M = len(grid[0])
    dp = [[0 for _ in range(M + 2)] for _ in range(N + 2)]  # add top and bottom 0 padding

    for r in range(1, N + 1):   # Set the base case. Could prob be cleaner
        for c in range(1, M + 1):
            if grid[r - 1][c - 1] == pattern[0]:
                dp[r][c] = 1
    for i in range(1, len(pattern)):
        # print(dp)
        # Need a new cache. Otherwise, we will have dirty cache reads.
        newDp = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                if pattern[i] == grid[r - 1][c - 1]:
                    top, right = dp[r - 1][c], dp[r][c + 1]
                    bottom, left = dp[r + 1][c], dp[r][c - 1]
                    
                    newDp[r][c] = max(top, right, bottom, left)
        dp = newDp
    # print(dp)
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if dp[r][c] == 1:
                return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
