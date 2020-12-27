from typing import List

from test_framework import generic_test

def search_smallest(A: List[int]) -> int:

    low = 0
    high = len(A) - 1

    while low < high:

        mid = low + (high-low) // 2

        if A[mid] > A[high]:
            low  = mid +1
        else:
            high = mid

    return high


#def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    #return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
