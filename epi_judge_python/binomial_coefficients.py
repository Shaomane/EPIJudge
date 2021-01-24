from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    # TODO - you fill in here.
    if k == 0: 
        return 1

    pTriangle = [ [0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range (len(pTriangle)):
        pTriangle[i][0] = 1

    for r in range(1, n + 1):
        for c in range(1, k + 1):
            pTriangle[r][c] = pTriangle[r - 1][c - 1] + pTriangle[r - 1][c]
    
    return pTriangle[n][k]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
