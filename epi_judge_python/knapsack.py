import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    # TODO - you fill in here.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    
    for r in range(1, len(items) + 1):
        for c in range(1, capacity + 1):
            currentAdd = 0
            if c - items[r - 1].weight >= 0:
                currentAdd = dp[r][c - items[r - 1].weight] + items[r - 1].value

            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1], currentAdd)

    return dp[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
