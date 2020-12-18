from typing import List

from test_framework import generic_test


def multiply(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.

    sign = -1 if ( (A[0] < 0) ^ (B[0] < 0) ) else 1

    A[0], B[0] = abs(A[0]), abs(B[0])

    result = [0 for _ in range(len(A) + len(B))]

    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i + j +1] += A[i] * B[j]
            result[i+j] += result[i + j + 1] // 10
            result[ i + j + 1 ] %= 10

    result = result[next((i for i, x in enumerate(result) if x !=0),len(result)):] or [0]

    result[0] *= sign

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
