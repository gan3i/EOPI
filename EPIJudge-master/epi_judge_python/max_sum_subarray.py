from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # TODO - you fill in here.
    max_seen = max_end = 0 

    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_end, max_seen)
    return max_seen


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
