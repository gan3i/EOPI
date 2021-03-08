from test_framework import generic_test
import functools
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    if num_as_string =='0':
        return num_as_string

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()),num_as_string[is_negative:],0)

    result = []
    convert_to_base(num_as_int, b2, result)

    # while num_as_int:
    #     result.append(string.hexdigits[num_as_int % b2].upper())
    #     num_as_int //= b2

    # if is_negative:
    #     result.append('-')

    # return ''.join(reversed(result))

    return ('-' if is_negative else '') + ''.join(result)

def convert_to_base(num_as_int, base, result):
    if num_as_int == 0:
        return 
    else:
        convert_to_base(num_as_int // base, base, result)
        result.append(string.hexdigits[num_as_int % base].upper())

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
