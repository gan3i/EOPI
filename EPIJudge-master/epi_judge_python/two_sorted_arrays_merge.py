from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # TODO - you fill in here.
    end = m + n -1
    m , n = m -1, n-1
    while m >= 0 and n >= 0:
        if A[m] < B[n]:
            A[end] = B[n]
            end -=1
            n -= 1
        else:
            A[end] = A[m]
            end -=1
            m -= 1

    while n >= 0:
        A[end] = B[n]
        end -=1
        n -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
