from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    if n == 1 or m == 1:
        return 1

    # we really only want the first row and column set to 1,
    # but it doesn't matter if we set the rest as well since they get overwritten.
    dp = [[1] * (m)] * (n)
    for r in range(1, n):
        for c in range(1, m):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[n - 1][m - 1]

if __name__ == '__main__':
    exit(›
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
