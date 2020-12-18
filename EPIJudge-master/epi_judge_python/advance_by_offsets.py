from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    furth_most  = 0
    i = 0
    last_index = len(A) - 1


    while i <= furth_most & furth_most < last_index:
        furth_most = max(furth_most, A[i] + i)
        i += 1

    if furth_most < last_index:
        return False   

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
