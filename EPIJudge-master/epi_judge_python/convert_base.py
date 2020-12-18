from test_framework import generic_test
import functools
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    def construct_from_base(num_as_int, base):
        if num_as_int == 0:
            return ''
        else:
            return construct_from_base(num_as_int // base, base) + string.hexdigits[num_as_int % base].upper()


    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(lambda x, c : x * b1 + string.hexdigits.index(c.lower()),num_as_string[is_negative:],0)

    return ('-' if is_negative else '')  + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
