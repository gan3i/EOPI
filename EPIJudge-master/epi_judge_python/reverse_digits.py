from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    sign = 1
    if x < 0:
        sign = -1
        x *=-1

    result = 0

    while x :
        mod = x % 10
        result = (result * 10) + mod
        x =x//10

    return result * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
