from test_framework import generic_test

def square_root( k :int) -> int:

    if k <=1:
        return k
    low = 1
    high = k

    while low < high -1:

        mid = low + (high - low)//2

        if mid ** 2 > k:
            high = mid
        elif mid ** 2 < k:
            low = mid
        else:
            return mid

    return low




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
