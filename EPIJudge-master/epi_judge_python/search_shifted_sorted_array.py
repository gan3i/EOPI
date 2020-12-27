from typing import List

from test_framework import generic_test

def search_smallest(A: List[int]) -> int:

    low = 0 
    high = len(A) - 1

    if high == 0:
        return low

    if A[low] < A[high]:
        return low

    while low < high - 1:

        mid = low + (high-low) // 2

        if A[mid-1] > A[mid] < A[mid+1]:
            return mid
        elif A[mid] < A[0]:
            high = mid
        else:
            low = mid

    return high


#def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    #return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
