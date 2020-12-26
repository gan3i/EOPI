from typing import List
import bisect

from test_framework import generic_test

def search_first_of_k(A: List[int],target: int) -> int:

    if not A:
        return -1
    #--------------------------------
    # index =  bisect.bisect_left(A,target)

    # return index if index < len(A) and A[index] == target else -1
    #-----------------------------------

    low = 0
    high = len(A) - 1

    while low <= high:
        mid = low + (high-low) // 2

        if A[mid] == target:
            if mid == 0 or A[mid-1] != A[mid]:
                return mid
            else:
                high = mid - 1
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1 

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
