from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    if x == 0:
        return '0'
    start = ord('0')
    sign = 1
    if x<0:
        sign = -1
        x= x * sign
    result = []
    while x:
        result.append(chr(start + x % 10))
        x = x // 10
    if sign < 0:
        result.append('-')
    return ''.join(x for x in reversed(result))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    i = 0
    sign = 1 
    start = ord('0')
    if s[0] == '-':
        i += 1
        sign = -1
    if s[0] == '+':
        i += 1
    result = 0
    while i < len(s):
        result = result * 10 + (ord(s[i])- start)
        i +=1

    return result * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')
wrapper(4176473, '4176473')

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
